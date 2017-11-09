import oslo_messaging
import sys, os, time, threading

basedir = os.path.dirname(os.path.abspath(__file__))
os.chdir(basedir)
sys.path.append(basedir)
sys.path.append(os.path.join(basedir, '..'))

from config import CONF

class Client(object):

	def __init__(self):
		transport = oslo_messaging.get_rpc_transport(CONF)
		target = oslo_messaging.Target(topic='agent')
		self.client = oslo_messaging.RPCClient(transport, target)

	def test(self):
		ctxt = {}
		arg = 0
		while True:
			self.client.call(ctxt, 'test', arg=arg)
			arg += 1
			time.sleep(2)

	def stop_server(self):
		ctxt = {}	
		target = self.client.prepare(namespace='control', version='2.0')
		target.call(ctxt, 'stop')

client = Client()
thread1 = threading.Thread(target=client.test, name='client.test', daemon=False)
thread2 = threading.Thread(target=client.stop_server, name='client.stop_server', daemon=False)
thread1.start()
thread2.start()
thread1.join()
thread2.join()





