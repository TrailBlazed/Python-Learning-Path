# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:02:10 2021

@author: tskir
"""

""" Add and update values in a set"""
s={"a","b","c","d"}
print("Original set")
print(s)
s.add('e')
print("Print the set after adding a value")
print(s)

"""Update through another set or List"""
r={"e","f"}
print("Adding values from set")
s.update(r)
print(s)
q=["g","h"]
print("Adding values from list")
s.update(q)
print(s)



