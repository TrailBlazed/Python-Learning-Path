# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:18:29 2021

@author: tskir
"""

"""Lambda Example"""
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
z=lambda x,y: x+y
print("z has x+y:{}".format(z(x,y)))
y=lambda x:x*5
print("y*5:{}".format(y(x)))




