'''
Created on 2015年1月9日

@author: kingsoft
'''
import time
import _thread
import threading
import random

list = []
exitFlag = 0
lock = threading.Lock()
MAX_COUNT = 20

class CustomerThread(threading.Thread):
    
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        while not exitFlag:
            lock.acquire()
            if len(list) > 0:
                item = list[0]
                list.remove(item)
                print("customer %s --->%s"%(self.name,item))
            lock.release()
            time.sleep(0.001 * random.randint(0,10))

class ProviderThread(threading.Thread):
    
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        
    def run(self):
        global  itemNum
        while exitFlag == 0 and itemNum < MAX_COUNT:
            time.sleep(0.001 * random.randint(0,10))
            numLock.acquire()
            item = '%d'%(itemNum)
            itemNum += 1
            numLock.release()
            
            lock.acquire()
            list.append(item)
            print("Provider %s --->%s"%(self.name,item))
            lock.release()
            


itemNum = 0;
numLock = threading.Lock()

customerCount = 100
providerCount = 10

threads = []

for i in range(0,customerCount):
    thread = CustomerThread("%d"%(i))
    thread.start()
    threads.append(thread)

for i in range(0,providerCount):
    thread = ProviderThread("%d"%(i))
    thread.start()
    threads.append(thread)    

while True:
    time.sleep(1)
    if len(list) == 0 and itemNum > MAX_COUNT:
        break
exitFlag = 1

for thread in threads:
    thread.join()
    
print("Exiting Main Thread")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        