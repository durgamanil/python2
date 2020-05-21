# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 07:56:48 2020

@author: Onyx1
"""

from threading import *
import time
import random
import queue

def produce(q):
    while True:
        item=random.randint(1,100)
        print("producer producing item",item)
        q.put(item)
        print("producer giving notification")
        time.sleep(5)

def consume(q): 
    while True:
        print("consumer waiting for updation")
        print("consumer consuming items:",q.get())
        time.sleep(5)
        

q=queue.Queue()
t1=Thread(target=consume,args=(q,))
t2=Thread(target=produce,args=(q,))
t1.start()
t2.start()
