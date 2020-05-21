# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 07:46:59 2019

@author: Onyx1
"""

a=input("Enter some string::")
i=0
print("The Characters at even positions:")
while i<len(a):
    print(a[i],end=',')
    i=i+2
i=1
print()
print("The Characters at odd positions:")
while i<len(a):
    print(a[i],end=',')
    i=i+2