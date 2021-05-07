# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:29:40 2021

@author: tskir
"""

"""Ques 14: Find the denomination"""
p=int(input("Enter the value"))
h=int(p//100)
a=p%100
f=int(a//50)
b=a%50
t=int(b//20)
c=b%20
te=int(c//10)
d=c%10



print("{} number of $100".format(h))
print("{} number of $50".format(f))
print("{} number of $20".format(t))
print("{} number of $10".format(te))
print("{} number of $1".format(d))