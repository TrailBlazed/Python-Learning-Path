# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:12:58 2021

@author: tskir
"""

"""Ques2:Print Ascii Value of the Character and vice-versa"""
alpha='a'
b=0
b=ord(alpha) 
#ord() is the function used to convert char to int because int(alpha) will throw error
print("ASCII of a is:",b)
alpha1=chr(b)
print("int to ASCII for 97 is:",alpha1)
#chr() is the function used to convert int to char 