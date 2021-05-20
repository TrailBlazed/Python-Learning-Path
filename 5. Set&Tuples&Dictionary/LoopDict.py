# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:11:17 2021

@author: tskir
"""

s={1:"a",2:"b",3:"c",4:"d"}
print("Loop for keys:")
for x in s.keys():
    print(x)
print("Loop for values:")
for x in s.values():
    print(x)
print("Loop through items in the dictionary:")
for x,y in s.items():
    print("key={} and its value={}".format(x,y))





