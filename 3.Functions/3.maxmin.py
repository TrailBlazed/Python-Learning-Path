# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:35:50 2021

@author: tskir
"""

"""3.Find maximum and minimum between two numbers using functions"""

def minmax(a,b):
    if(a>b):
        print("Greater number is {} and smaller one is {}".format(a,b))
    else:
        print("Greater number is {} and smaller one is {}".format(b,a))

a=int(input("Enter a number"))
b=int(input("Enter another number"))
minmax(a,b)