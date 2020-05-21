# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:16:34 2019

@author: anil durgam
"""
s= input("Enter some string:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+previous*(int(x)-1)
print(output)



    
