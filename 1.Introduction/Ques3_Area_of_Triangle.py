# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:24:07 2021

@author: tskir
"""

"""Ques 3: Area of Triangle """

a=float(input("Enter the first side:"))
b=float(input("Enter the second side:"))
c=float(input("Enter the third side:"))
s=(a+b+c)/2
area=((s*(s-a)*(s-b)*(s-c))**0.5)
print("Area of Triangle:%3.2f" %area)




