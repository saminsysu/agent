import os
import oslo_messaging
import time
from endpoints import endpoints, ServerControlEndpoint
import sys

basedir = os.path.dirname(os.path.abspath(__file__))
os.chdir(basedir)
sys.path.append(basedir)
sys.path.append(os.path.join(basedir, '..'))

from config import CONF

transport = oslo_messaging.get_rpc_transport(CONF)
target = oslo_messaging.Target(topic='agent', server='server1')
server = oslo_messaging.get_rpc_server(transport, target, endpoints,
                                       executor='threading')
ServerControlEndpoint.server = server

try:
	server.start()
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print("Stopping server1")

server.stop()
server.wait()