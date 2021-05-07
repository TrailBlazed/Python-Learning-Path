# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:03:47 2021

@author: tskir
"""

def add(x):
    z=x+20
    return z
def sub(x):
    u=x-10
    return u

x=10
print("Function composition:",add(sub(x)))



    