# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:32:44 2021

@author: tskir
"""

"""Ques 9: Input month number and print number of days in that month.
lets consider yeap year for Feb """
a=31
b=30
c=28
d=29
m=str(input("Enter first 3 letter of month for number of days: "))
y=int(input("Enter year please: "))
if(m=="jan" or m=="mar" or m=="may" or m=="jul" or m=="aug" or m=="oct" or m=="dec"):
    print(a)
elif(m=="apr" or m=="jun" or m=="sep" or m=="nov"):
    print(b)
elif(m=="feb"):
    if(y%4==0 and y%100!=100):
        if(y%400==0):
            print(c)
        else:
            print(d)
    