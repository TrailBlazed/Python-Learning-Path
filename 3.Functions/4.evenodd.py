# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:43:59 2021

@author: tskir
"""

"""4.A number is even or odd using functions."""
def evenodd(a):
    if(a%2==0):
        print("{} is even".format(a))
    else:
        print("{} is odd".format(a))
        
a=int(input("Enter a number:"))
evenodd(a)