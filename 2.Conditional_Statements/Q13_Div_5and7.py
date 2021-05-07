# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:17:48 2021

@author: tskir
"""

"""Q13:Check whether a number is divisible by 5 and 11 or not."""
a=int(input("Enter a number: "))
if((a%5==0) and (a%11==0)):
    print("Yes, its divisible by 5 and 11")
else:
    print("No, its not divisible by 5 and 11")