# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:57:02 2021

@author: tskir
"""

"""Q4:A Character Is an Alphabet or Not, Uppercase, Lowercase, Special Character, or Digit"""
ch=ord(input("Enter a value:"))
ch1=chr(ch)

if(ch>=97 and ch<=122 or ch>=65 and ch<=90):
    print("%c is an Alphabet" %ch1)
    if(ch>=97 and ch<=122):
        print("%c is also lowercase"%ch1)
    elif(ch>=65 or ch<=90):
        print("%c is also uppercase:" %ch1)
elif(ch>=48 and ch<=59):
    print("%c is a number" %ch1)
elif(ch>=32 and ch<=47 or ch>=60 and ch<=64 or ch>=91 and ch<=96 or ch>=123 and ch<=127 ):
    print("%c is special character" %ch1)
    

