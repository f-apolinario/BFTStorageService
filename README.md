# BFTStorageService
BFTStorageService is a byzantine fault tolerant API written in Python for clients to store and read data in several Key Value Stores (KVS) while being resilient to byzantine failures.

This API provides 4 operations to the client:
-write (key, value) - writes value under the key into a quorum of 3f+1 KVS so that the value is present in the majority of KVSs of the quorum. In order to tolerate f Byzantine Failures.

-read (key) - read value of the corresponding key from a majority of the quorum,  so that the value is present in the majority of KVSs of the quorum. Thus becoming resilient to Byzantine Failures.

-delete (key, value) - deletes value under the key from a quorum of 3f+1 KVS so that the value is no longer present in the majority of KVSs of the quorum. In order to tolerate f Byzantine Failures.

-list () -NOT YET IMPLEMENTED - Lists the keys present in the majority of the quorum, i.e. the retrievable keys 

##Install:
This service is to be installed on the clients and on the servers
###Server
Use folder server:
####configuration File
Configure config.json with the ip of the server and port the service will use
####Run
run command:
python StorageService.py
###Client
Use folder client:
####configuration File
Configure config.json with:
"servers": amount of servers the client will use
"KVS_IPS": array of pairs ("ip" and "port") one for each server the client will use
####Integrate API
>from BftStorageService import *
