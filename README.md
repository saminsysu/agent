agent
======

概述
------

agent分服务器端和客户端，使用oslo.messaging实现服务器和客户端解耦，主要是实现RPC调用，使用rabbitmq做消息队列。

安装rabbitmq
------------

参照http://rabbitmq.mr-ping.com/installation/Installing_on_Debian_Ubuntu.html

安装完成后添加用户rabbitmqctl add_user agent admin123，并赋予权限rabbitmqctl set_permissions -p / agent ".*" ".*" ".*"
