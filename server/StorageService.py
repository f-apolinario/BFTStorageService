import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import json
import KVSHandler as handler

with open('config.json') as d:
	config = json.load(d)

ip = config['ip']
port = int(config['port'])

def write(key, value):
	global handler
	return handler.write(key,value)

def delete(key):
	global handler
	return handler.delete(key)

def list():
   	global handler
	return handler.list()

def read(key):
	global handler
	return handler.read(key)

server = SimpleXMLRPCServer((ip, port), allow_none=True)
print "Listening on port " + str(port) +  "..."

server.register_function(write, "write")
server.register_function(delete, "delete")
server.register_function(list, "list")
server.register_function(read, "read")

server.serve_forever()
