# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 23:23:46 2019

@author: Onyx1
"""
l1=[10,20,30,40,50,60,70]
x=int(input("enter elements to be removed"))
if x in l1:
    l1.remove(x)
    print("removed successfully")
    print(l1)
else:
    print("specified element is not available")