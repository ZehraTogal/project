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

zehra@zehra-VirtualBox:~$ pip3 install ryu

Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: ryu in ./.local/lib/python3.8/site-packages (4.34)
Requirement already satisfied: eventlet!=0.18.3,!=0.20.1,!=0.21.0,!=0.23.0,>=0.18.2 in ./.local/lib/python3.8/site-packages (from ryu) (0.30.2)
Requirement already satisfied: msgpack>=0.3.0 in ./.local/lib/python3.8/site-packages (from ryu) (1.1.1)
Requirement already satisfied: netaddr in ./.local/lib/python3.8/site-packages (from ryu) (1.3.0)
Requirement already satisfied: oslo.config>=2.5.0 in ./.local/lib/python3.8/site-packages (from ryu) (9.6.0)
Requirement already satisfied: ovs>=2.6.0 in ./.local/lib/python3.8/site-packages (from ryu) (3.6.1)
Requirement already satisfied: routes in ./.local/lib/python3.8/site-packages (from ryu) (2.5.1)
Requirement already satisfied: six>=1.4.0 in /usr/lib/python3/dist-packages (from ryu) (1.14.0)
Requirement already satisfied: tinyrpc in ./.local/lib/python3.8/site-packages (from ryu) (1.1.7)
Requirement already satisfied: webob>=1.2 in ./.local/lib/python3.8/site-packages (from ryu) (1.8.9)
Requirement already satisfied: dnspython<2.0.0,>=1.15.0 in ./.local/lib/python3.8/site-packages (from eventlet!=0.18.3,!=0.20.1,!=0.21.0,!=0.23.0,>=0.18.2->ryu) (1.16.0)
Requirement already satisfied: greenlet>=0.3 in ./.local/lib/python3.8/site-packages (from eventlet!=0.18.3,!=0.20.1,!=0.21.0,!=0.23.0,>=0.18.2->ryu) (3.1.1)
Requirement already satisfied: PyYAML>=5.1 in /usr/lib/python3/dist-packages (from oslo.config>=2.5.0->ryu) (5.3.1)
Requirement already satisfied: debtcollector>=1.2.0 in ./.local/lib/python3.8/site-packages (from oslo.config>=2.5.0->ryu) (3.0.0)
Requirement already satisfied: oslo.i18n>=3.15.3 in ./.local/lib/python3.8/site-packages (from oslo.config>=2.5.0->ryu) (6.4.0)
Requirement already satisfied: requests>=2.18.0 in /usr/lib/python3/dist-packages (from oslo.config>=2.5.0->ryu) (2.22.0)
Requirement already satisfied: rfc3986>=1.2.0 in ./.local/lib/python3.8/site-packages (from oslo.config>=2.5.0->ryu) (2.0.0)
Requirement already satisfied: stevedore>=1.20.0 in ./.local/lib/python3.8/site-packages (from oslo.config>=2.5.0->ryu) (5.3.0)
Requirement already satisfied: sortedcontainers in ./.local/lib/python3.8/site-packages (from ovs>=2.6.0->ryu) (2.4.0)
Requirement already satisfied: repoze.lru>=0.3 in ./.local/lib/python3.8/site-packages (from routes->ryu) (0.7)
Requirement already satisfied: wrapt>=1.7.0 in ./.local/lib/python3.8/site-packages (from debtcollector>=1.2.0->oslo.config>=2.5.0->ryu) (2.0.1)
Requirement already satisfied: pbr>=2.0.0 in ./.local/lib/python3.8/site-packages (from oslo.i18n>=3.15.3->oslo.config>=2.5.0->ryu) (7.0.3)
Requirement already satisfied: setuptools in /usr/lib/python3/dist-packages (from pbr>=2.0.0->oslo.i18n>=3.15.3->oslo.config>=2.5.0->ryu) (45.2.0)
zehra@zehra-VirtualBox:~$
