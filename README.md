zehra@zehra-VirtualBox:~$ sudo mn --topo single,3 --mac --switch ovsk --controller remote,ip=127.0.0.1,port=6654
[sudo] password for zehra: 
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 
*** Adding switches:
s1 
*** Adding links:
(h1, s1) (h2, s1) (h3, s1) 
*** Configuring hosts
h1 h2 h3 
*** Starting controller
c0 
*** Starting 1 switches
s1 ...
*** Starting CLI:
mininet-wifi> nodes
available nodes are: 
c0 h1 h2 h3 s1
mininet-wifi> 

-------------------------
zehra@zehra-VirtualBox:~$ ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13
loading app ryu.app.simple_switch_13
loading app ryu.controller.ofp_handler
instantiating app ryu.app.simple_switch_13 of SimpleSwitch13
instantiating app ryu.controller.ofp_handler of OFPHandler
packet in 1 00:00:00:00:00:03 33:33:ff:00:00:03 3
packet in 1 00:00:00:00:00:03 33:33:00:00:00:16 3
packet in 1 00:00:00:00:00:02 33:33:00:00:00:16 2
packet in 1 00:00:00:00:00:02 33:33:ff:00:00:02 2
packet in 1 00:00:00:00:00:01 33:33:00:00:00:16 1
packet in 1 00:00:00:00:00:01 33:33:00:00:00:16 1
packet in 1 00:00:00:00:00:01 33:33:00:00:00:02 1
packet in 1 00:00:00:00:00:03 33:33:00:00:00:16 3
packet in 1 00:00:00:00:00:03 33:33:00:00:00:02 3
packet in 1 00:00:00:00:00:03 33:33:00:00:00:16 3
packet in 1 00:00:00:00:00:01 33:33:00:00:00:16 1
packet in 1 00:00:00:00:00:02 33:33:00:00:00:16 2
packet in 1 00:00:00:00:00:02 33:33:00:00:00:02 2
packet in 1 00:00:00:00:00:02 33:33:00:00:00:16 2
packet in 1 00:00:00:00:00:02 33:33:00:00:00:02 2
packet in 1 00:00:00:00:00:03 33:33:00:00:00:02 3
packet in 1 00:00:00:00:00:01 33:33:00:00:00:02 1
packet in 1 00:00:00:00:00:02 33:33:00:00:00:02 2
packet in 1 00:00:00:00:00:01 33:33:00:00:00:02 1
packet in 1 00:00:00:00:00:03 33:33:00:00:00:02 3
packet in 1 00:00:00:00:00:03 33:33:00:00:00:02 3
packet in 1 00:00:00:00:00:02 33:33:00:00:00:02 2
packet in 1 00:00:00:00:00:01 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:02 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:ff:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:ff:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:02 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:ff:00:00:01 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:ff:00:00:03 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1 00:00:00:00:00:02 33:33:00:00:00:02 2
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:02 1
packet in 1 00:00:00:00:00:03 33:33:00:00:00:02 3
packet in 1 00:00:00:00:00:01 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:02 00:00:00:00:00:03 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1 00:00:00:00:00:02 33:33:00:00:00:02 2
packet in 1 00:00:00:00:00:03 33:33:00:00:00:02 3
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:02 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:02 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:16 1
packet in 1 00:00:00:00:00:01 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:16 1
packet in 1152921504606846977 00:00:00:00:00:03 33:33:00:00:00:02 1
packet in 1152921504606846977 00:00:00:00:00:03 ff:ff:ff:ff:ff:ff 1
packet in 1152921504606846977 00:00:00:00:00:02 33:33:00:00:00:02 1

----------------------------------------
zehra@zehra-VirtualBox:~$ sudo python3 mobilityModel.py
[sudo] password for zehra: 
*** Node'lar oluşturuluyor
*** Node'lar yapılandırılıyor
*** ap1-wlan1: minimum tx power (1 dBm) yields 40.00m for requested 40.00m (delta +0.00m)
*** sta1-wlan0: minimum tx power (1 dBm) yields 116.13m for requested 35.00m (delta +81.13m)
*** sta2-wlan0: minimum tx power (1 dBm) yields 116.13m for requested 35.00m (delta +81.13m)
📐 PropagationModel: logDistance (exp=3.0)
✅ RemoteController eklendi: 127.0.0.1:6654
*** Ağ başlatılıyor
✅ ap1 Ryu Controller'a bağlandı (tcp:127.0.0.1:6654)
⚠️ sta1 sinyali ZAYIFLADI (GERÇEK RSSI=-73 dBm ≤ -70) → TxPower artırma isteği gönderildi
⚠️ sta2 sinyali ZAYIFLADI (GERÇEK RSSI=-74 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=30.34m | GERÇEK RSSI=-73 dBm
📡 sta2 | mesafe=31.64m | GERÇEK RSSI=-74 dBm
*** CLI çalıştırılıyor
*** Starting CLI:
stopping sta1 
stopping sta2 
---------------------------------------------
[IZLEME] sta1: RSSI=-73 dBm | Loss=100.0% | Durum=OK | TX: 100 mBm
[IZLEME] sta2: RSSI=-74 dBm | Loss=100.0% | Durum=OK | TX: 100 mBm
[OZET] Worst RSSI: -74 dBm | Worst Loss: 100.0%
-> [AKSIYON] TX artırıldı: 600 mBm
mininet-wifi> 🔧 ap1 TxPower güncellendi → 6 dBm
📶 sta1 sinyali tekrar İYİ (GERÇEK RSSI=-67 dBm > -70)
📶 sta2 sinyali tekrar İYİ (GERÇEK RSSI=-69 dBm > -70)
📡 sta1 | mesafe=29.24m | GERÇEK RSSI=-67 dBm
📡 sta2 | mesafe=33.42m | GERÇEK RSSI=-69 dBm
📡 sta1 | mesafe=27.04m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=33.97m | GERÇEK RSSI=-69 dBm
⚠️ sta2 sinyali ZAYIFLADI (GERÇEK RSSI=-70 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=25.38m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=35.34m | GERÇEK RSSI=-70 dBm
🔧 ap1 TxPower güncellendi → 11 dBm
📡 sta1 | mesafe=28.31m | GERÇEK RSSI=-62 dBm
📡 sta2 | mesafe=36.33m | GERÇEK RSSI=-65 dBm
📶 sta2 sinyali tekrar İYİ (GERÇEK RSSI=-66 dBm > -70)
📡 sta1 | mesafe=33.12m | GERÇEK RSSI=-64 dBm
📡 sta2 | mesafe=37.52m | GERÇEK RSSI=-66 dBm
📡 sta1 | mesafe=38.05m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=38.71m | GERÇEK RSSI=-66 dBm
📡 sta1 | mesafe=38.64m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=39.71m | GERÇEK RSSI=-66 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=33.35m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=41.50m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=20.69m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=43.33m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=32.83m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=42.45m | GERÇEK RSSI=-67 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=34.07m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=39.53m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=20.90m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=36.60m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=32.44m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=33.90m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=38.13m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=32.23m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=28.14m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=35.10m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=34.60m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=38.38m | GERÇEK RSSI=-67 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=36.24m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=41.30m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=39.05m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=43.37m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=36.41m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=41.93m | GERÇEK RSSI=-67 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=33.79m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=39.55m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=34.00m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=36.76m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=36.75m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=33.59m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=31.02m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=35.01m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=28.52m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=36.41m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=32.70m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=38.23m | GERÇEK RSSI=-67 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=39.08m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=40.68m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=30.57m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=41.32m | GERÇEK RSSI=-67 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=29.48m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=39.64m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=37.41m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=38.26m | GERÇEK RSSI=-67 dBm
📴 sta1, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=39.82m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=37.06m | GERÇEK RSSI=-67 dBm
✅ sta1, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=33.06m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=34.98m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=24.36m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=36.27m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=24.56m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=39.57m | GERÇEK RSSI=-67 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=24.75m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=42.84m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=33.01m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=41.57m | GERÇEK RSSI=-67 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=37.07m | GERÇEK RSSI=-66 dBm
📡 sta2 | mesafe=38.20m | GERÇEK RSSI=-67 dBm
📡 sta1 | mesafe=36.58m | GERÇEK RSSI=-66 dBm
