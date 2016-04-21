# BFTStorageService

BFTStorageService is a byzantine fault tolerant API written in Python for clients to store and read data in several Key Value Stores (KVS) while being resilient to byzantine failures.

This API provides 4 operations to the client:

- `write (key, value)`: Writes a value under the key into a quorum of 3f+1 KVS so that the value is present in the majority of KVSs of the quorum. In order to tolerate f Byzantine Failures.

- `read (key)`: Reads the value of the corresponding key from a majority of the quorum, so that the value is present in the majority of KVSs of the quorum. Thus becoming resilient to Byzantine Failures.

- `delete (key, value)`: Deletes a value under the key from a quorum of 3f+1 KVS so that the value is no longer present in the majority of KVSs of the quorum. In order to tolerate f Byzantine Failures.

- `list ()`: **[NOT YET IMPLEMENTED]** Lists the keys present in the majority of the quorum, i.e. the retrievable keys 

## Install:

This service needs to be installed on the client machines and on the server machines.

### Server

- Go to server folder.
- Configure config.json with the IP of the server and port the service will use.
- Run command:

```
  python StorageService.py
```

### Client

- Go to client folder.
- Configure config.json with:

```
  "servers": amount of servers the client will use.
  "KVS_IPS": array of pairs ("ip" and "port") one for each server the client will use.
```

- Integrate API into code with:

```
  from BftStorageService import *
```
