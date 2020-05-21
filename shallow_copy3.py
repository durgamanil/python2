# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 06:57:57 2020

@author: Onyx1
"""
import copy

l1=[10,20,[30,40],50]
#l2=l1.copy()
#it dnot work for list inside another list
l2=copy.copy(l1)

l2[2][0]=70
print("l2:",l2)
print("l1:",l1)