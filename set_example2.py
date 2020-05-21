# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:32:48 2020

@author: Onyx1
"""

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
print(b)