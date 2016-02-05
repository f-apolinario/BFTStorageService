kvs = {}

def read(key):
	global kvs
	return kvs.get(key, None)

def write(key, value):
	global kvs
	kvs[key] = value;
	return True

def delete(key):
	global kvs
	del kvs[key]
	return True

def list():
	global kvs
	return kvs.keys()
