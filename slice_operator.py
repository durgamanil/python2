# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 06:53:23 2019

@author: anil
Topic:slice operator

"""
a='0123456789'
#a[begin index:end index:direction]
#begin index start from zero
#end index goes upto length of the string.in my case it is ten
#the last parameter indicates the direction if that is '+' its mean positive direction
#if that is '-' then negative direction and also step to increse
print(a[0:11:1])
#in end index forward direction then it should be '-1' need to delete
print(a[0:11:2])
print(a[0:11:3])
print(a[0:11:4])
print(a[0:11:5])
print(a[0:11:6])
print(a[0:11:7])
print(a[0:11:8])
print(a[0:11:9])

#begin index from different values
print()
print("slice operator begin value from different indexes")
print(a[1:11:2])
print(a[1:11:3])
print(a[1:11:4])


