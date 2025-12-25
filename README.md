شغّلي Ryu (زي ما عندك على 6654):

ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13


افتحي Terminal ثاني وشغّلي Mininet:

sudo mn --topo single,3 --mac --switch ovsk --controller remote,ip=127.0.0.1,port=6654
