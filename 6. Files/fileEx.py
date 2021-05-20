# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:59:06 2021

@author: tskir
"""

"""File Handling"""
print("Creating the file with x")
f=open("hello.txt","x")
print("Yes!Created")
f.close()

print("Now writing to the file...")
f=open("hello.txt","w")
f.write("Hello")
f.write("\n")
f.write("Kiran\n")
f.close()

print("Now appending to the file...")
with open("hello.txt","a",encoding="utf-8") as f:
    f.write("Hi\n")
    f.write("Sarada")


t=open("hello.txt","r")
print("Reading first 5 characters")
print(t.read(5))
t.close()

t=open("hello.txt","r")
print("Read all the characters")
print(t.read())
t.close()



