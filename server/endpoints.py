import oslo_messaging



class ServerControlEndpoint(object):

    target = oslo_messaging.Target(namespace='control',
                                   version='2.0')
    server = None

    @classmethod
    def stop(cls, ctx):
        if cls.server:
            cls.server.stop()
            print("Stopping server1")
        else:
            print("No server to stop")

    @property
    def server(self, server):
        ServerControlEndpoint.server = server 

class TestEndpoint(object):

    def test(self, ctx, arg):
        print(arg)

endpoints = [
    ServerControlEndpoint(),
	TestEndpoint(),
]