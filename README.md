zehra@zehra-VirtualBox:~$ ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13
loading app ryu.app.simple_switch_13
loading app ryu.controller.ofp_handler
instantiating app ryu.app.simple_switch_13 of SimpleSwitch13
instantiating app ryu.controller.ofp_handler of OFPHandler
^Czehra@zehra-VirtualBox:~$ 

-------------------------------------------
zehra@zehra-VirtualBox:~$ sudo python3 mobilityModel.py
[sudo] password for zehra: 
*** Node'lar oluşturuluyor
*** Node'lar yapılandırılıyor
*** ap1-wlan1: minimum tx power (1 dBm) yields 40.00m for requested 40.00m (delta +0.00m)
*** sta1-wlan0: minimum tx power (1 dBm) yields 116.13m for requested 35.00m (delta +81.13m)
*** sta2-wlan0: minimum tx power (1 dBm) yields 116.13m for requested 35.00m (delta +81.13m)
📐 PropagationModel: logDistance (exp=3.0)
*** Ağ başlatılıyor
📡 sta1 | mesafe=70.71m | RSSI(GERÇEK)=NA
📡 sta2 | mesafe=70.71m | RSSI(GERÇEK)=NA
*** CLI çalıştırılıyor
*** Starting CLI:
mininet-wifi> ✅ sta1, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=29.96m | RSSI(GERÇEK)=-73 dBm
⚠️ sta1 sinyali ZAYIFLADI (RSSI(GERÇEK)=-73 dBm ≤ -70) → TxPower artırma isteği gönderildi
✅ sta2, ap1 kapsama alanına GİRDİ
⚠️ sta2 sinyali ZAYIFLADI (RSSI(GERÇEK)=-74 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta2 | mesafe=33.61m | RSSI(GERÇEK)=-74 dBm
📡 sta1 | mesafe=27.32m | RSSI(GERÇEK)=-72 dBm
📡 sta2 | mesafe=33.77m | RSSI(GERÇEK)=-74 dBm
📶 sta1 sinyali tekrar GÜÇLÜ/İYİ (RSSI(GERÇEK)=-66 dBm > -70)
📡 sta1 | mesafe=25.38m | RSSI(GERÇEK)=-66 dBm
📡 sta2 | mesafe=35.34m | RSSI(GERÇEK)=-70 dBm
📡 sta1 | mesafe=29.10m | RSSI(GERÇEK)=-67 dBm
📡 sta2 | mesafe=36.53m | RSSI(GERÇEK)=-70 dBm
⚠️ sta1 sinyali ZAYIFLADI (RSSI(GERÇEK)=-70 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=34.75m | RSSI(GERÇEK)=-70 dBm
📡 sta2 | mesafe=37.92m | RSSI(GERÇEK)=-71 dBm
📡 sta1 | mesafe=38.05m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=38.71m | RSSI(GERÇEK)=-71 dBm
📡 sta1 | mesafe=39.55m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=39.90m | RSSI(GERÇEK)=-72 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=30.62m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=42.08m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=20.94m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=43.42m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=24.59m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=43.79m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=24.59m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=43.79m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=35.57m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=41.87m | RSSI(GERÇEK)=-72 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
⚠️ sta2 sinyali ZAYIFLADI (RSSI(GERÇEK)=-72 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=31.38m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=38.94m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=22.36m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=36.21m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=34.96m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=33.32m | RSSI(GERÇEK)=-72 dBm
📴 sta1, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=40.83m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=31.97m | RSSI(GERÇEK)=-72 dBm
✅ sta1, ap1 kapsama alanına GİRDİ
⚠️ sta1 sinyali ZAYIFLADI (RSSI(GERÇEK)=-71 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=32.58m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=33.76m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=28.25m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=36.83m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=34.95m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=38.96m | RSSI(GERÇEK)=-72 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=37.29m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=42.46m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=38.96m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=42.63m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=35.83m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=41.76m | RSSI(GERÇEK)=-72 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
⚠️ sta2 sinyali ZAYIFLADI (RSSI(GERÇEK)=-72 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=33.87m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=39.75m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=33.90m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=36.96m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=36.32m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=33.57m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=30.75m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=35.11m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=28.21m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=36.98m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=37.89m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=39.73m | RSSI(GERÇEK)=-72 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=31.87m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=41.54m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=27.59m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=40.04m | RSSI(GERÇEK)=-72 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
⚠️ sta2 sinyali ZAYIFLADI (RSSI(GERÇEK)=-72 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=35.75m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=38.51m | RSSI(GERÇEK)=-72 dBm
📴 sta1, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=40.55m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=37.21m | RSSI(GERÇEK)=-72 dBm
✅ sta1, ap1 kapsama alanına GİRDİ
⚠️ sta1 sinyali ZAYIFLADI (RSSI(GERÇEK)=-71 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=37.51m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=34.55m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=27.43m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=35.75m | RSSI(GERÇEK)=-72 dBm
📡 sta1 | mesafe=23.38m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=38.74m | RSSI(GERÇEK)=-72 dBm
---------------------------------------------
[IZLEME] sta1: RSSI=N/A | Loss=30.0% | Durum=RSSI yok (bağlı değil/menzil dışı)
[IZLEME] sta2: RSSI=-72 dBm | Loss=0.0% | Durum=OK | TX: 100 mBm
[OZET] Worst RSSI: -72 dBm | Worst Loss: 30.0%
-> [AKSIYON] TX artırıldı: 1100 mBm
📶 sta1 sinyali tekrar GÜÇLÜ/İYİ (RSSI(GERÇEK)=-64 dBm > -70)
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=24.75m | RSSI(GERÇEK)=-65 dBm
📡 sta2 | mesafe=42.84m | RSSI(GERÇEK)=NA
⚠️ sta1 sinyali ZAYIFLADI (RSSI(GERÇEK)=-71 dBm ≤ -70) → TxPower artırma isteği gönderildi
✅ sta2, ap1 kapsama alanına GİRDİ
⚠️ sta2 sinyali ZAYIFLADI (RSSI(GERÇEK)=-71 dBm ≤ -70) → TxPower artırma isteği gönderildi
📡 sta1 | mesafe=39.37m | RSSI(GERÇEK)=-71 dBm
📡 sta2 | mesafe=36.88m | RSSI(GERÇEK)=-71 dBm
📶 sta1 sinyali tekrar GÜÇLÜ/İYİ (RSSI(GERÇEK)=-68 dBm > -70)
📡 sta1 | mesafe=30.43m | RSSI(GERÇEK)=-68 dBm
📡 sta2 | mesafe=38.19m | RSSI(GERÇEK)=-71 dBm
🔧 ap1 TxPower güncellendi → 11 dBm
📡 sta1 | mesafe=24.22m | RSSI(GERÇEK)=-60 dBm
📡 sta2 | mesafe=37.90m | RSSI(GERÇEK)=-66 dBm
📶 sta2 sinyali tekrar GÜÇLÜ/İYİ (RSSI(GERÇEK)=-65 dBm > -70)
📡 sta1 | mesafe=25.69m | RSSI(GERÇEK)=-61 dBm
📡 sta2 | mesafe=36.43m | RSSI(GERÇEK)=-65 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=30.26m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=42.66m | RSSI(GERÇEK)=-67 dBm
📴 sta1, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=43.75m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=31.93m | RSSI(GERÇEK)=-67 dBm
✅ sta1, ap1 kapsama alanına GİRDİ
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=29.69m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=42.92m | RSSI(GERÇEK)=-67 dBm
📡 sta1 | mesafe=21.37m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=44.06m | RSSI(GERÇEK)=-67 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=29.02m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=34.94m | RSSI(GERÇEK)=-67 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=36.76m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=43.00m | RSSI(GERÇEK)=-67 dBm
📴 sta1, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=40.76m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=34.21m | RSSI(GERÇEK)=-67 dBm
✅ sta1, ap1 kapsama alanına GİRDİ
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=32.95m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=39.02m | RSSI(GERÇEK)=-67 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=37.42m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=40.65m | RSSI(GERÇEK)=-67 dBm
📡 sta1 | mesafe=23.49m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=35.67m | RSSI(GERÇEK)=-67 dBm
📡 sta1 | mesafe=31.22m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=35.28m | RSSI(GERÇEK)=-67 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=36.50m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=42.58m | RSSI(GERÇEK)=-67 dBm
✅ sta2, ap1 kapsama alanına GİRDİ
📡 sta1 | mesafe=21.47m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=37.71m | RSSI(GERÇEK)=-67 dBm
📡 sta1 | mesafe=33.71m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=42.46m | RSSI(GERÇEK)=-67 dBm
📡 sta1 | mesafe=29.52m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=36.66m | RSSI(GERÇEK)=-67 dBm
📴 sta2, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU
📡 sta1 | mesafe=35.31m | RSSI(GERÇEK)=-64 dBm
📡 sta2 | mesafe=34.86m | RSSI(GERÇEK)=-67 dBm
📴 sta1, ap1 kapsama alanından ÇIKTI → SİNYAL KOPTU

[1]+  Stopped                 sudo python3 mobilityModel.py
zehra@zehra-VirtualBox:~$ 

