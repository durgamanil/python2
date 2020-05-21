# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:24:23 2020

@author: Onyx1
"""

from threading import *
import time

def wish(name):
    for i in range(10):
        print("good afternoon:",end='')
        time.sleep(2)
        print(name)

t1=Thread(target=wish,args=('anil'))
t2=Thread(target=wish,args=('vishnu'))
t1.start()
t2.start()

    