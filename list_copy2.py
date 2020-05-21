# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:51:05 2019

@author: Onyx1
"""

x=[10,20,30,40]
y=x[:]
print(x)
y[1]=111
print(id(x))
print(id(y))
print(y)
print(x)