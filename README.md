sudo python3 mobilityModel.py
-------------
sudo ss -lntp | grep 6653
sudo lsof -i :6653
sudo kill -9 12345
ryu-manager ryu.app.simple_switch_13
ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13
py from mininet.node import RemoteController
py c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6654)
py ap1.start([c0])
sudo ss -lntp | grep 6653
