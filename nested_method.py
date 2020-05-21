# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 07:41:29 2020

@author: Onyx1
"""

class test():
    def m1(self):
        def calculate(a,b):
            print("sum:",a+b)
            print("dif:",a-b)
            print("division",a/b)
            print("product:",a*b)
            print()
        calculate(10,20)
        calculate(100,200)
        calculate(1000,2000)

t= test()
t.m1()
        