# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:58:29 2019

@author: anildurgam
"""
s1=input("enter the first string::")
s2=input("enter the second string::")
output=''
i=j=0
while i<len(s1) or j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j+1
print(output)
