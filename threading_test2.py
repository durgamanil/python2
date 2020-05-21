# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 07:50:09 2020

@author: Onyx1
"""

from threading import *
import time
e=Event()
def consumer():
    print("consumer thread is waiting for updation")

    e.wait()
    print("consumer got notification and consuming items")

def producer():
    time.sleep(5)
    print("priducer thread is producing items")
    print("producer thread giving notification by setting  event")
    e.set()
    
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()
    
