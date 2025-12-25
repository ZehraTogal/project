#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    # روابط (لتثبيت الاتصال وقياس ping/loss بشكل أوضح)
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)

    # RSSI واقعي عبر نموذج انتشار
    try:
        net.setPropagationModel(model="logDistance", exp=3.0)
        info("📐 PropagationModel: logDistance (exp=3.0)\n")
    except Exception as e:
        info(f"⚠️ setPropagationModel uygulanamadı: {e}\n")

    # ملاحظة: plotGraph + Thread + setTxPower قد يعمل مشاكل
    # لو بدك رسومات شغل مع -p لتجنب الرسم.
    if '-p' not in args:
        net.plotGraph()

    net.setMobilityModel(
        time=0, model='RandomDirection',
        max_x=100, max_y=100, seed=20
    )

    info("*** Ağ başlatılıyor\n")
    net.build()
    ap1.start([])

    # ✅ أعطي AP IP حتى نقدر نعمل ping لقياس Loss%
    try:
        ap1.setIP('10.0.0.1/8', intf=ap1.wintfs[0].name)
    except Exception:
        pass

    AP_IP = "10.0.0.1"

    # -------------------------
    # RSSI (حقيقي)
    # -------------------------
    def get_real_rssi(sta):
        # 1) Mininet-WiFi
        try:
            r = getattr(sta.wintfs[0], "rssi", None)
            if r is not None:
                return int(r)
        except Exception:
            pass

        # 2) iw link
        try:
            iface = sta.wintfs[0].name
            out = sta.cmd(f"iw dev {iface} link 2>/dev/null")
            m = re.search(r"signal:\s*(-?\d+)\s*dBm", out)
            if m:
                return int(m.group(1))
        except Exception:
            pass

        return None

    # -------------------------
    # TX power (station) -> mBm
    # -------------------------
    def get_tx_mbm(sta):
        try:
            iface = sta.wintfs[0].name
            out = sta.cmd(f"iw dev {iface} info 2>/dev/null")
            # txpower 23.00 dBm
            m = re.search(r"txpower\s+([0-9.]+)\s*dBm", out)
            if m:
                dbm = float(m.group(1))
                return int(round(dbm * 100))  # mBm = 100 * dBm
        except Exception:
            pass
        return None

    # -------------------------
    # Loss% via ping parsing
    # -------------------------
    def get_loss_percent(sta, dst_ip, count=3, timeout=1):
        """
        إذا sta خارج المدى/غير مرتبط => ping يرجع 100% عادة.
        """
        try:
            out = sta.cmd(f"ping -c {count} -W {timeout} {dst_ip} 2>/dev/null")
            # "3 packets transmitted, 3 received, 0% packet loss"
            m = re.search(r"(\d+)%\s*packet loss", out)
            if m:
                return float(m.group(1))
        except Exception:
            pass
        return 100.0

    # -------------------------
    # Safe TxPower change (avoid update_graph thread issues)
    # -------------------------
    def safe_set_ap_txpower(ap, new_power_dbm):
        try:
            # مؤقتاً عطّل update_graph لتجنب مشاكل الـ thread/plotGraph
            old_update_graph = getattr(ap, "update_graph", None)
            try:
                ap.update_graph = lambda *a, **k: None
            except Exception:
                pass

            ap.setTxPower(new_power_dbm, intf=ap.wintfs[0].name)

            if old_update_graph is not None:
                try:
                    ap.update_graph = old_update_graph
                except Exception:
                    pass
            return True
        except Exception as e:
            info(f"⚠️ TxPower değiştirilemedi: {e}\n")
            return False

    # -------------------------
    # Monitor printing in the requested format
    # -------------------------
    def monitor_like_output(ap, stations, interval=1.5):
        RSSI_WARN = -70
        RSSI_CRIT = -80
        LOSS_CRIT = 30.0

        POWER_STEP = 5
        MAX_TXPOWER = 30

        while True:
            worst_rssi = None
            worst_loss = 0.0

            info("---------------------------------------------\n")

            for s in stations:
                rssi = get_real_rssi(s)
                loss = get_loss_percent(s, AP_IP, count=3, timeout=1)

                if rssi is None:
                    durum = "RSSI yok (bağlı değil/menzil dışı)"
                    rssi_str = "N/A"
                    # لو RSSI غير موجود غالباً Loss=100
                    loss = 100.0
                else:
                    if rssi <= RSSI_CRIT:
                        durum = "COK ZAYIF"
                    elif rssi <= RSSI_WARN:
                        durum = "ZAYIF"
                    else:
                        durum = "OK"
                    rssi_str = f"{rssi} dBm"

                tx_mbm = get_tx_mbm(s)
                tx_part = f" | TX: {tx_mbm} mBm" if tx_mbm is not None else ""

                info(f"[IZLEME] {s.name}: RSSI={rssi_str} | Loss={loss:.1f}% | Durum={durum}{tx_part}\n")

                # تحديث worst
                if rssi is not None:
                    if (worst_rssi is None) or (rssi < worst_rssi):
                        worst_rssi = rssi
                if loss > worst_loss:
                    worst_loss = loss

            worst_rssi_print = worst_rssi if worst_rssi is not None else "N/A"
            info(f"[OZET] Worst RSSI: {worst_rssi_print} | Worst Loss: {worst_loss:.1f}\n")

            # قرار/أكشن
            action_done = False
            if worst_rssi is not None and worst_rssi <= RSSI_CRIT:
                # ارفع TX
                cur = getattr(ap.wintfs[0], "txpower", 20)
                newp = min(cur + POWER_STEP, MAX_TXPOWER)
                if newp != cur:
                    ok = safe_set_ap_txpower(ap, newp)
                    if ok:
                        info(f"-> [AKSIYON] TxPower artırıldı: {cur} -> {newp} dBm\n")
                        action_done = True

            if (not action_done) and (worst_loss >= LOSS_CRIT):
                # Loss عالي جداً، جرّب رفع TX أيضاً
                cur = getattr(ap.wintfs[0], "txpower", 20)
                newp = min(cur + POWER_STEP, MAX_TXPOWER)
                if newp != cur:
                    ok = safe_set_ap_txpower(ap, newp)
                    if ok:
                        info(f"-> [AKSIYON] Loss yüksek, TxPower artırıldı: {cur} -> {newp} dBm\n")
                        action_done = True

            if not action_done:
                info("-> [AKSIYON] Stabil (değişiklik yok)\n")

            time.sleep(interval)

    t = threading.Thread(
        target=monitor_like_output,
        args=(ap1, [sta1, sta2]),
        daemon=True
    )
    t.start()

    info("*** CLI çalıştırılıyor\n")
    CLI(net)

    info("*** Ağ durduruluyor\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)
