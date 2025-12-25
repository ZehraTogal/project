ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13
sudo mn --topo single,3 --mac --switch ovsk --controller remote,ip=127.0.0.1,port=6654
sudo python3 mobilityModel.py
