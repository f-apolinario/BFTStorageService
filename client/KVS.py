import xmlrpclib as rpc_handle
class KVS:
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.connection = rpc_handle.ServerProxy("http://" + ip + ":" + port + "/", allow_none = True)

	def write(self,key,value):
		return self.connection.write(key, value)

	def read(self,key):
		return self.connection.read(key)

	def list(self):
		return self.connection.list()

	def delete(self,key):
		return self.connection.delete(key)
