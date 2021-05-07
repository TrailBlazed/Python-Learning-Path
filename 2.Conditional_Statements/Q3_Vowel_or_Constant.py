# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:21:59 2021

@author: tskir
"""
"""Q3:Character Is Vowel or Consonant"""

ch=str(input("Enter a character:"))
if(ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
    print("The character entered in Vowel")
else:
    print("The character entered %c is Consonant" %ch)