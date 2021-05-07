# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:44:47 2021

@author: tskir
"""

"""Q5:Leap Year"""
""" Algo: should be divisible by 400 or when divisible by 4 should not be divisible by 100"""
y=int(input("Enter an year:"))
if(y%400==0 ):
    if(y%4==0 and y!=100):
        print("%d is leap year" %y)
else:
    print("%d is not leap year" %y)