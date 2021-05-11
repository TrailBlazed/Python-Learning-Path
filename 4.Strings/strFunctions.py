# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:43:45 2021

@author: tskir
"""

greet = "hello world!"
g=["a","b","c"] #sequence of string to join
j="*"
greet1="PYTHON PROGRAMMING" 
print("To Upper:",greet.upper()) #convert to upppercase
print("To Lower:",greet1.lower()) #convert to lowercase
print("Is AlphNumeric?",greet.isalnum())	#only alphanumeric characters (no symbols)
print("Is Alpha:",greet1.isalpha())	#only alphabetic characters (no symbols)
print("Is Lower:",greet.islower())	#alphabetic characters are all lower case
print("Is Numeric:",greet.isnumeric())	#only numeric characters
print("Is whitespace:",greet.isspace())	#only whitespace characters
print("Is Title Case:",greet.istitle())	#In title case
print("Is Upper:",greet.isupper())	#alphabetic characters are all upper case
print("Length of greet:",len(greet)) #find length of string
print("Join demo:", j.join(g)) #join the list of string with the help of delimiter 
print("Split Demo:",greet.split(" ")) # split the string into list of strings with the delimiter
print("Replace Demo:",greet.replace("hello","Hi")) # replace value in the string



