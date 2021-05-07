# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:35:56 2021

@author: tskir
"""
i=0
turns=0
while(turns<5):
    print("in While Loop")
    i=int(input("Enter 4 to continue"))
    if(i<=4): 
        print("I not printed")
        print("turns=",turns)
        continue  # do not break from loop
    print("i=",i)
    turns=turns+1
    print("turns=",turns)
  
print("Sorry you ran out of turns")