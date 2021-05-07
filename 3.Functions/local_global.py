# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:30:16 2021

@author: tskir
"""

x=300   #Global declaration of x

def test1():
    print("x=",x) #calling global x
    
def test2():
    x=100  #local variable x
    print("x=",x) #will print the local variable value
    
test1()
test2()    
    