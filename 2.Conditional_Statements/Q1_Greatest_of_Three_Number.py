# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:02:38 2021

@author: tskir
"""

"""Ques 1:The Greatest Number Among the Given Three Number"""
a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter the third number"))
if(a>b):
    if(a>c):
        print("First number is greatest:",a)
    else:
        print("Third number is greatest:",b)
elif(b>c):
    print("Second number is greatest:",b)
else:
    print("Third number is greatest:",c)