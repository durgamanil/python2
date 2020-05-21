# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:16:18 2019

@author: anil durgam
program:
    write a program to search the vowel in the given string
    
"""
vowels=['a','e','i','o','u']
word=input("enter the some word to search for vowels\n")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("the number of different vowels present in",word,"is:",len(found) )


