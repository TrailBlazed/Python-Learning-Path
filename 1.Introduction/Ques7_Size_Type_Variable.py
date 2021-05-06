# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:07:14 2021

@author: tskir
"""

"""Ques 7: Determine the size and type of a variable"""
"""Important note: 
   int	 28 bytes
   float 26 bytes
   str	 49	+1 per additional character (49+total length of characters) """
from sys import getsizeof
a=3
b=2.6
c="Hello"
d='d'
print("a is of type:",type(a),"and of size is:",getsizeof(a))
print("b is of type:",type(b),"and of size is:",getsizeof(b))
print("c is of type:",type(c),"and of size is:",getsizeof(c))
print("d is of type:",type(d),"and of size is:",getsizeof(d))