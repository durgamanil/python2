# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:17:06 2020

@author: Onyx1
"""

import queue
q=queue.LifoQueue()
q.put(10)
q.put(20)
q.put(15)
q.put(30)
q.put(0)
while not q.empty():
    print(q.get(),end=' ')