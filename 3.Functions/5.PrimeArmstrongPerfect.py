# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:52:58 2021

@author: tskir
"""

"""5.A number is prime, Armstrong or perfect number using functions"""
import math
def armstrong(x):
    arm=0
    while(x>0):
        q=x%10
        arm=arm+math.pow(q,3)
        x=x//10
    return arm

def perfect(x):
    per=0
    i=1
    while(i<x):
        if(x%i==0):
            per=per+i
        i=i+1
    return per
def prime(x):
    i=2
    for i in range(2,x):
        if(x%i==0):
            return True
        else:
            return False
x=int(input("Enter a number:"))
arm=int(armstrong(x))
per=int(perfect(x))
prime=bool(prime(x))
if(arm==x):
    print("The {} is armstrong number".format(arm))
else:
    print("The number is not armstrong")

if(per==x):
    print("The {} is perfect".format(per))
else:
    print("The number is not perfect")

if(prime!=True):
    print("{} is prime".format(x))
else:
    print("The number is not armstrong or not perfect or prime")
