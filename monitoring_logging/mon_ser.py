import sys
sys.path.insert(0, "../communication_module")


import communication_module
##server
import time
import os
import ast 
import pymongo
from _thread import *
import threading 

from time import sleep
from json import dumps
from kafka import KafkaProducer
from kafka import KafkaConsumer

from kafka import KafkaConsumer
from json import loads
from json import dumps
from kafka import KafkaProducer


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["hackdb"]



def eventReceiveRuntimeServerToMonMod(m1):
    print("receieved:::",m1)
    message = m1
    res = ast.literal_eval(message) 
    print("Message receieved:",(res),type(res))
    mycol = mydb["mon_data"]
    # mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(res)


fun3=eventReceiveRuntimeServerToMonMod


def threaded_servers():
	print ("In thread servers")
	while True:
		# sleep(1)
		communication_module.Runtime_Servers_to_Monitoring_Module_interface(fun3)




start_new_thread(threaded_servers,()) 



while(1):
	pass



'''Topics req
commonLog
deploymentMonitoring
monitoringDeployment

schedulerMonitoring
monitoringScheduler

'''