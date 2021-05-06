# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:35:36 2021

@author: tskir
"""

"""Ques 9: Converting Temperature Celsius into Fahrenheit and vice-versa
(32°F − 32) × 5/9 = 0°C
(30°C x 1.8) + 32 = 86°F"""

f=float(input("Enter the Fahrenheit:"))
c=float(input("Enter the Celsius:"))
calc_c=(f-32)*5/9
calc_f=(c*1.8)+32
print("Fahrenheit for",f,"Celsius is:",calc_c)
print("Celsius for",c," Fahrenheit is:",calc_f)
