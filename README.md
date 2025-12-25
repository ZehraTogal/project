#!/usr/bin/env python

"Node'ların konumlarını ayarlama ve hareket (mobility) modelleri sağlama"

import sys
import time
import threading
import math
import re

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(args):
    "Bir ağ oluşturur."
    net = Mininet_wifi()

    info("*** Node'lar oluşturuluyor\n")

    STA_RANGE = 35

    sta1 = net.addStation(
        'sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8',
        min_x=10, max_x=30, min_y=50, max_y=70, min_v=5, max_v=10
    )
    sta2 = net.addStation(
        'sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8',
        min_x=60, max_x=70, min_y=10, max_y=20, min_v=1, max_v=5
    )

    AP_RANGE = 40

    if '-m' in args:
        ap1 = net.addAccessPoint(
            'ap1', wlans=2, ssid='ssid1,ssid2', mode='g',
            channel='1', failMode="standalone",
            position='50,50,0',
            range=AP_RANGE
        )
    else:
        ap1 = net.addAccessPoint(
            'ap1', ssid='new-ssid', mode='g', channel='1',
            failMode="standalone", position='50,50,0',
            range=AP_RANGE
        )

    info("*** Node'lar yapılandırılıyor\n")
    net.configureNodes()

    sta1.setRange(STA_RANGE)
    sta2.setRange(STA_RANGE)

    # ✅ RSSI'nin gerçekçi olması için Mininet-WiFi propagation model seç (opsiyonel ama önerilir)
    # Bu model RSSI değerlerini kendisi üretir.
    try:
        net.setPropagationModel(model="logDistance", exp=3.0)
        info("📐 PropagationModel: logDistance (exp=3.0)\n")
    except Exception as e:
        info(f"⚠️ setPropagationModel uygulanamadı: {e}\n")

    if '-p' not in args:
        net.plotGraph()

    net.setMobilityModel(
        time=0, model='RandomDirection',
        max_x=100, max_y=100, seed=20
    )

    info("*** Ağ başlatılıyor\n")
    net.build()
    ap1.start([])

    # ✅✅✅ GERÇEK RSSI OKUMA
    def get_real_rssi(sta):
        # 1) Mininet-WiFi'nin güncel tuttuğu RSSI
        try:
            r = getattr(sta.wintfs[0], "rssi", None)
            if r is not None:
                return int(r)
        except Exception:
            pass

        # 2) iw çıktısından okumayı dene (arayüz içinde)
        try:
            iface = sta.wintfs[0].name
            out = sta.cmd(f"iw dev {iface} link 2>/dev/null")
            m = re.search(r"signal:\s*(-?\d+)\s*dBm", out)
            if m:
                return int(m.group(1))
        except Exception:
            pass

        return None

    # ---- TxPower değişikliğini thread'den main thread'e taşımak için istek kutusu
    tx_lock = threading.Lock()
    tx_request = {"new_power": None}

    def request_txpower_increase(ap, step=5, max_txpower=30):
        with tx_lock:
            current = ap.wintfs[0].txpower
            new_power = current + step
            if new_power > max_txpower:
                new_power = max_txpower
            tx_request["new_power"] = new_power

    def apply_txpower_if_requested(ap):
        with tx_lock:
            new_power = tx_request["new_power"]
            tx_request["new_power"] = None

        if new_power is not None:
            ap.setTxPower(new_power, intf=ap.wintfs[0].name)
            info(f"🔧 {ap.name} TxPower güncellendi → {new_power} dBm\n")

    def monitor_ap_range_and_rssi(ap, stations, interval=0.5):
        ap_range = ap.wintfs[0].range

        RSSI_CRIT = -70
        RSSI_WEAK = -80

        POWER_STEP = 5
        MAX_TXPOWER = 30

        status = {s.name: None for s in stations}
        weak_state = {s.name: False for s in stations}

        while True:
            for s in stations:
                dist = s.get_distance_to(ap)
                inside = (dist <= ap_range)

                if status[s.name] is None:
                    status[s.name] = inside
                else:
                    if inside and not status[s.name]:
                        info(f"✅ {s.name}, {ap.name} kapsama alanına GİRDİ\n")
                        status[s.name] = True
                        weak_state[s.name] = False
                    elif (not inside) and status[s.name]:
                        info(f"📴 {s.name}, {ap.name} kapsama alanından ÇIKTI → SİNYAL KOPTU\n")
                        status[s.name] = False
                        weak_state[s.name] = False

                if not inside:
                    continue

                # ✅ هنا بدل التخمين: نقرأ RSSI الحقيقي
                rssi_val = get_real_rssi(s)
                if rssi_val is None:
                    info(f"❔ {s.name} RSSI okunamadı (mesafe={dist:.2f}m)\n")
                    continue

                if rssi_val <= RSSI_CRIT and not weak_state[s.name]:
                    info(f"⚠️ {s.name} sinyali ZAYIFLADI (RSSI(GERÇEK)={rssi_val} dBm ≤ {RSSI_CRIT}) → TxPower artırma isteği gönderildi\n")
                    weak_state[s.name] = True
                    request_txpower_increase(ap, step=POWER_STEP, max_txpower=MAX_TXPOWER)

                if rssi_val > RSSI_CRIT and weak_state[s.name]:
                    info(f"📶 {s.name} sinyali tekrar GÜÇLÜ/İYİ (RSSI(GERÇEK)={rssi_val} dBm > {RSSI_CRIT})\n")
                    weak_state[s.name] = False

                if rssi_val <= RSSI_WEAK:
                    info(f"🚨 {s.name} sinyali ÇOK ZAYIF (RSSI(GERÇEK)={rssi_val} dBm)\n")

            time.sleep(interval)

    def rssi_measurement(ap, stations, interval=0.5):
        while True:
            for s in stations:
                dist = s.get_distance_to(ap)
                rssi_val = get_real_rssi(s)
                if rssi_val is None:
                    info(f"📡 {s.name} | mesafe={dist:.2f}m | RSSI(GERÇEK)=NA\n")
                else:
                    info(f"📡 {s.name} | mesafe={dist:.2f}m | RSSI(GERÇEK)={rssi_val} dBm\n")
            time.sleep(interval)

    t1 = threading.Thread(
        target=monitor_ap_range_and_rssi,
        args=(ap1, [sta1, sta2]),
        daemon=True
    )
    t1.start()

    t2 = threading.Thread(
        target=rssi_measurement,
        args=(ap1, [sta1, sta2]),
        daemon=True
    )
    t2.start()

    info("*** CLI çalıştırılıyor\n")
    CLI(net)

    apply_txpower_if_requested(ap1)

    info("*** Ağ durduruluyor\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
