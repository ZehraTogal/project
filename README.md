sudo python3 mobilityModel.py
-------------
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

zehra@zehra-VirtualBox:~$ 
