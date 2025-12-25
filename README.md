zehra@zehra-VirtualBox:~$ sudo python3 mobilityModel.py
[sudo] password for zehra: 
*** Node'lar oluşturuluyor
*** Node'lar yapılandırılıyor
*** ap1-wlan1: minimum tx power (1 dBm) yields 40.00m for requested 40.00m (delta +0.00m)
*** sta1-wlan0: minimum tx power (1 dBm) yields 116.13m for requested 35.00m (delta +81.13m)
*** sta2-wlan0: minimum tx power (1 dBm) yields 116.13m for requested 35.00m (delta +81.13m)
📐 PropagationModel: logDistance (exp=3.0)
*** Ağ başlatılıyor
📡 sta1 | mesafe=70.71m | RSSI(GERÇEK)=0 dBm
📡 sta2 | mesafe=70.71m | RSSI(GERÇEK)=0 dBm
*** CLI çalıştırılıyor
*** Starting CLI:
stopping sta1 
stopping sta2 
---------------------------------------------
[IZLEME] sta1: RSSI=0 dBm | Loss=100.0% | Durum=OK | TX: 100 mBm
[IZLEME] sta2: RSSI=0 dBm | Loss=100.0% | Durum=OK | TX: 100 mBm
[OZET] Worst RSSI: 0 dBm | Worst Loss: 100.0%
-> [AKSIYON] Stabil (değişiklik yok)
mininet-wifi> ✅ sta1, ap1 kapsama alanına GİRDİ
⚠️ sta1 sinyali ZAYIFLADI (RSSI(GERÇEK)=-73 dBm ≤ -70) → TxPower artırma isteği gönderildi
✅ sta2, ap1 kapsama alanına GİRDİ
⚠️ sta2 sinyali ZAYIFLADI (RSSI(GERÇEK)=-74 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=30.34m | RSSI(GERÇEK)=-73 dBm
📡 sta2 | mesafe=31.64m | RSSI(GERÇEK)=-74 dBm
📡 sta1 | mesafe=28.90m | RSSI(GERÇEK)=-72 dBm
📡 sta2 | mesafe=33.33m | RSSI(GERÇEK)=-74 dBm
📡 sta1 | mesafe=26.76m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=34.16m | RSSI(GERÇEK)=-75 dBm
📡 sta1 | mesafe=25.79m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=34.95m | RSSI(GERÇEK)=-75 dBm
📡 sta1 | mesafe=27.53m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=36.14m | RSSI(GERÇEK)=-75 dBm
📡 sta1 | mesafe=33.12m | RSSI(GERÇEK)=-74 dBm
📡 sta2 | mesafe=37.52m | RSSI(GERÇEK)=-76 dBm
📡 sta1 | mesafe=38.05m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=38.71m | RSSI(GERÇEK)=-76 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=38.82m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=40.30m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=31.53m | RSSI(GERÇEK)=-73 dBm
📡 sta2 | mesafe=41.90m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=24.28m | RSSI(GERÇEK)=-70 dBm
📡 sta2 | mesafe=42.97m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=24.28m | RSSI(GERÇEK)=-70 dBm
📡 sta2 | mesafe=42.97m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=24.28m | RSSI(GERÇEK)=-70 dBm
📡 sta2 | mesafe=42.97m | RSSI(GERÇEK)=0 dBm
📶 sta1 sinyali tekrar GÜÇLÜ/İYİ (RSSI(GERÇEK)=-68 dBm > -70)
📡 sta1 | mesafe=20.94m | RSSI(GERÇEK)=-68 dBm
📡 sta2 | mesafe=43.42m | RSSI(GERÇEK)=0 dBm
⚠️ sta1 sinyali ZAYIFLADI (RSSI(GERÇEK)=-72 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=28.25m | RSSI(GERÇEK)=-72 dBm
📡 sta2 | mesafe=43.44m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=37.41m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=41.47m | RSSI(GERÇEK)=0 dBm
Exception in thread wifiParameters:
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 932, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.8/threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.8/dist-packages/mininet_wifi-2.7-py3.8.egg/mn_wifi/mobility.py", line 175, in parameters
    self.config_links(mob_nodes)
  File "/usr/local/lib/python3.8/dist-packages/mininet_wifi-2.7-py3.8.egg/mn_wifi/mobility.py", line 199, in config_links
    ack = self.check_in_range(intf, ap_intf)
  File "/usr/local/lib/python3.8/dist-packages/mininet_wifi-2.7-py3.8.egg/mn_wifi/mobility.py", line 143, in check_in_range
    self.ap_out_of_range(intf, ap_intf)
  File "/usr/local/lib/python3.8/dist-packages/mininet_wifi-2.7-py3.8.egg/mn_wifi/mobility.py", line 109, in ap_out_of_range
    intf.disconnect(ap_intf)
  File "/usr/local/lib/python3.8/dist-packages/mininet_wifi-2.7-py3.8.egg/mn_wifi/link.py", line 533, in disconnect
    self.iwdev_cmd('{} disconnect'.format(self.name))
  File "/usr/local/lib/python3.8/dist-packages/mininet_wifi-2.7-py3.8.egg/mn_wifi/link.py", line 117, in iwdev_cmd
    return self.cmd('iw dev', *args)
  File "/usr/local/lib/python3.8/dist-packages/mininet/link.py", line 70, in cmd
    return self.node.cmd( *args, **kwargs )
  File "/usr/local/lib/python3.8/dist-packages/mininet/node.py", line 386, in cmd
    self.sendCmd( *args, **kwargs )
  File "/usr/local/lib/python3.8/dist-packages/mininet/node.py", line 303, in sendCmd
    assert self.shell and not self.waiting
AssertionError
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=33.17m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=39.33m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=22.48m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=36.99m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=22.48m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=36.99m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=27.40m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=35.05m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=35.79m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=33.13m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=36.71m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=32.61m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=26.42m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=35.67m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=32.20m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=37.80m | RSSI(GERÇEK)=0 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=35.69m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=40.52m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=38.12m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=43.24m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=38.96m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=42.63m | RSSI(GERÇEK)=0 dBm
📡 sta1 | mesafe=34.63m | RSSI(GERÇEK)=-76 dBm
📡 sta2 | mesafe=40.94m | RSSI(GERÇEK)=0 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
