sudo python3 mobilityModel.py
-------------
zehra@zehra-VirtualBox:~$ py from mininet.node import RemoteController

Command 'py' not found, but can be installed with:

sudo apt install pythonpy

zehra@zehra-VirtualBox:~$ 
zehra@zehra-VirtualBox:~$ py c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6654)
bash: syntax error near unexpected token `('
zehra@zehra-VirtualBox:~$ py ap1.start([c0])
bash: syntax error near unexpected token `('
zehra@zehra-VirtualBox:~$ sudo ss -lntp | grep 6653
[sudo] password for zehra: 
LISTEN    0         10                 0.0.0.0:6653             0.0.0.0:*        users:(("ovs-testcontrol",pid=893,fd=3))                                       
zehra@zehra-VirtualBox:~$ 
-------------------------------
zehra@zehra-VirtualBox:~$ ryu-manager ryu.app.simple_switch_13
loading app ryu.app.simple_switch_13
loading app ryu.controller.ofp_handler
instantiating app ryu.app.simple_switch_13 of SimpleSwitch13
instantiating app ryu.controller.ofp_handler of OFPHandler
hub: uncaught exception: Traceback (most recent call last):
  File "/home/zehra/.local/lib/python3.8/site-packages/ryu/lib/hub.py", line 60, in _launch
    return func(*args, **kwargs)
  File "/home/zehra/.local/lib/python3.8/site-packages/ryu/controller/controller.py", line 152, in __call__
    self.server_loop(self.ofp_tcp_listen_port,
  File "/home/zehra/.local/lib/python3.8/site-packages/ryu/controller/controller.py", line 200, in server_loop
    server = StreamServer((CONF.ofp_listen_host,
  File "/home/zehra/.local/lib/python3.8/site-packages/ryu/lib/hub.py", line 127, in __init__
    self.server = eventlet.listen(listen_info)
  File "/home/zehra/.local/lib/python3.8/site-packages/eventlet/convenience.py", line 78, in listen
    sock.bind(addr)
OSError: [Errno 98] Address already in use

zehra@zehra-VirtualBox:~$ sudo ss -lntp | grep 6653
[sudo] password for zehra: 
LISTEN    0         10                 0.0.0.0:6653             0.0.0.0:*        users:(("ovs-testcontrol",pid=893,fd=3))                                       
zehra@zehra-VirtualBox:~$ sudo lsof -i :6653
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
ovs-testc 893 root    3u  IPv4  27136      0t0  TCP *:6653 (LISTEN)
zehra@zehra-VirtualBox:~$ sudo kill -9 12345
kill: (12345): No such process
zehra@zehra-VirtualBox:~$ ryu-manager ryu.app.simple_switch_13
loading app ryu.app.simple_switch_13
loading app ryu.controller.ofp_handler
instantiating app ryu.app.simple_switch_13 of SimpleSwitch13
instantiating app ryu.controller.ofp_handler of OFPHandler
hub: uncaught exception: Traceback (most recent call last):
  File "/home/zehra/.local/lib/python3.8/site-packages/ryu/lib/hub.py", line 60, in _launch
    return func(*args, **kwargs)
  File "/home/zehra/.local/lib/python3.8/site-packages/ryu/controller/controller.py", line 152, in __call__
    self.server_loop(self.ofp_tcp_listen_port,
  File "/home/zehra/.local/lib/python3.8/site-packages/ryu/controller/controller.py", line 200, in server_loop
    server = StreamServer((CONF.ofp_listen_host,
  File "/home/zehra/.local/lib/python3.8/site-packages/ryu/lib/hub.py", line 127, in __init__
    self.server = eventlet.listen(listen_info)
  File "/home/zehra/.local/lib/python3.8/site-packages/eventlet/convenience.py", line 78, in listen
    sock.bind(addr)
OSError: [Errno 98] Address already in use

zehra@zehra-VirtualBox:~$ ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13
loading app ryu.app.simple_switch_13
loading app ryu.controller.ofp_handler
instantiating app ryu.app.simple_switch_13 of SimpleSwitch13
instantiating app ryu.controller.ofp_handler of OFPHandler

