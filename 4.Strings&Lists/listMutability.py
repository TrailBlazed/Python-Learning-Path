# -*- coding: utf-8 -*-
"""
Created on Mon May 17 11:23:38 2021

@author: tskir
"""

"""Lists allow duplicates, add, remove and change"""
l=["a","b","c","d","a"]
print("*Dulicate values in the list*")
for i in range(0,len(l)):
    print("l{}:={}".format(i,l[i])) 
# changing a value in list
l[2]="z"
print("*A value location 2 changed in list*")
for i in range(0,len(l)):
    print("l{}:={}".format(i,l[i]))
print("*Remove a value from the list*")
l.remove("b")
for i in range(0,len(l)):
    print("l{}:={}".format(i,l[i]))
print("*Adding to the list*")
l.append("f")
for i in range(0,len(l)):
    print("l{}:={}".format(i,l[i]))






