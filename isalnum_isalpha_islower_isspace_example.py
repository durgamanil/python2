# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:54:15 2019

@author: anil durgam
"""

s=input("Enter any character:")
if s.isalnum():
    print("Alpha numeric character")
    if s.isalpha():
        print("Alphabet character")
        if s.islower():
            print("Lower case alphabet character")
        else:
            print("Upper case alphabet character")
    else:
        print("It is a digit")
elif s.isspace():
    print("It is space character")
else:
    print("Non space Special character")
    