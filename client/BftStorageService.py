import xmlrpclib
import socket
import json
from KVS import KVS

###################
#preparation phase#
###################

with open('config.json') as d:
	config = json.load(d)

#Total number of servers
n_servers = config["servers"]
#Total number of tolerated failures
f_servers = (n_servers - 1)/3

kvsArray = {}
for i in range(0, n_servers):
	c =  config['KVS_IPs'][i]
	kvsArray[i] = KVS(c['ip'], c['port'])

##################
#       API      #
##################

#write method - writes the value under the key in a majority (2*f+1) of the KVS
#in order to provide fault tolerance
def write(key,value):
	responses = 0
	i = 0

	while responses < (f_servers * 2 + 1) and  i < n_servers:
		try:
			kvsArray[i].write(key,value)
			status = True
			responses += 1
			i += 1
		except (socket.error):
			i += 1
	if responses < (f_servers * 2 + 1) :
		raise Exception('RemoteOperationException', 'Unable to perform the operation on a majority of storages. Expect errors while reading data.')
	return True


#delete method - deletes the value under the key in a majority (2*f+1) of the KVS
#in order to provide fault tolerance
def delete(key):
	responses = 0
	i = 0

	while responses < (f_servers * 2 + 1) and  i < n_servers:
		try:
			kvsArray[i].delete(key)
			status = True
			responses += 1
		except (socket.error):
			print "error"
		finally:
			i += 1
	if responses < (f_servers * 2 +1) :
		raise Exception('RemoteOperationException', 'Unable to perform the operation on a majority of storages. Expect errors while reading data.')
	return True

#read method - reads the value under the key from a majority (2*f+1) of the KVS
#until there is f+1 equal responses from the KVS.
#If f+1 equal responses is not possible the read operation throws an exception
def read(key):
	i = 0
	responses = {}
	n_responses = 0
	value = None

	while n_responses < (f_servers * 2 +1) and  i < n_servers:
		try:
			status = kvsArray[i].read(key)
			count = 1
			if responses.get(status) is not None:
				count += responses.get(status)
			responses[status] = count
			n_responses += 1
			if count >= f_servers + 1:
				return status
		except (socket.error):
			print "error"
		finally:
			i += 1
	raise Exception('RemoteOperationException', 'Unable to perform the operation on a majority of storages. Expect errors while reading data.')

def list():
	i = 0
	responses = []
	response_count = []
	n_responses = 0
	value = None
	while n_responses < (f_servers * 2 +1) and  i < n_servers:
		try:
			status = kvsArray[i].list()
			try:
				index = responses.index(set(status))
			except:
				index = -1
			count = 1
			if index != -1:
				count += response_count[index]
				response_count[index] = count
			else:
				responses.append(set(status))
				response_count.append(0)

			if count >= f_servers + 1:
				return status
		except (socket.error):
			print "error"
		finally:
			i += 1
	raise Exception('RemoteOperationException', 'Unable to perform the operation on a majority of storages. Expect errors while reading data.')

test_dict = {
		"key": "not the key",
		"not the value": "value",
		"asd": "dsa"
}

def main():
	for k, v in test_dict.items():
		print write(k, v)
		print read(k)

	print list()

	for k in test_dict.keys():
		print "Deleting ", k
		print delete(k)

if __name__ == "__main__":
    main()
