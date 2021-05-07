# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:04:39 2021

@author: tskir
"""

"""Q11: Find the maximum between the three numbers. """

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
if(a>b):
    if(a>c):
        print("{} is maximum number".format(a))
    else:
        print("{} is maximum number".format(c))
else:
    if(b>c):
        print("{} is maximum number".format(b))
    else:
        print("{} is maximum number".format(c))