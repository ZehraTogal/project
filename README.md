zehra@zehra-VirtualBox:~$ ryu-manager --ofp-tcp-listen-port 6654 ryu.app.simple_switch_13
loading app ryu.app.simple_switch_13
loading app ryu.controller.ofp_handler
instantiating app ryu.app.simple_switch_13 of SimpleSwitch13
instantiating app ryu.controller.ofp_handler of OFPHandler


-------------------
zehra@zehra-VirtualBox:~$ sudo ss -lntp | grep 6654
[sudo] password for zehra: 
LISTEN    0         50                 0.0.0.0:6654             0.0.0.0:*        users:(("ryu-manager",pid=4415,fd=4))                                          
zehra@zehra-VirtualBox:~$ 


----------------
zehra@zehra-VirtualBox:~$ c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6654)
bash: syntax error near unexpected token `('
zehra@zehra-VirtualBox:~$ 

