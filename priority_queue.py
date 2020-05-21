# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:28:48 2020

@author: Onyx1
"""

import queue
q=queue.PriorityQueue()
q.put(10)
q.put(20)
q.put(15)
q.put(30)
q.put(0)
while not q.empty():
    print(q.get(),end=' ')