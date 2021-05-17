# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:02:36 2021

@author: tskir
"""
"""Differenciating Aliasing and Cloning"""

"""Aliasing"""
l=["a","b","c"]
m=l  #aliasing 
print("List l is:")
for i in range(0,len(l)):
    print("l{}:={}".format(i,l[i]))
print("List m is:")
for i in range(0,len(m)):
    print("m{}:={}".format(i,m[i]))
    
#Changing a value in the aliased list m"
m[2]="z"
print("List l after changing value in m:")
for i in range(0,len(l)):
    print("l{}:={}".format(i,l[i]))

    
"""Cloning"""
l=["a","b","c"]
m=l[:] #cloning with slicing the list
print("List l is:")
for i in range(0,len(l)):
    print("l{}:={}".format(i,l[i]))
print("List m is:")
for i in range(0,len(m)):
    print("m{}:={}".format(i,m[i]))
    
print("Changing a value in the cloned list m:")
m[2]="z"
print("List l after changing value in m:")
for i in range(0,len(l)):
    print("l{}:={}".format(i,l[i]))