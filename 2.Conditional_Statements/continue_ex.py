# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:35:56 2021

@author: tskir
"""
i=0
turns=0
while(i<=5):
    print("in While Loop")
    i=int(input("Enter 4 to continue"))
    if(i==4): #looping contines more that 5 times if 4 pressed may times
        print("I not printed")
        continue
    else:
        print("i=",i)
        turns=turns+1
print("Sorry you ran out of turns")