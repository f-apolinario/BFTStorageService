from BftStorageService import * 
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
