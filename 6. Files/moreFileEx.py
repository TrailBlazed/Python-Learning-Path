# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:00:42 2021

@author: tskir
"""

"""More File Operations"""
try:
    f=open(r".\hello.txt","r")
    print("Yes!File Opened!!! \n")
    print("Read first 5 characters")    
    print(f.read(5))
    
    print("Read all characters")    
    print(f.read())
    
    print("\nSending back to pointer to the first character")
    print("Read Again!")
    f.seek(0)
    print(f.read())
    
    print("\nWhere is the cursor? {}".format(f.tell()))
    
    print("Reading n=3 lines")
    f.seek(0)
    for i in range(0,3):
        f1=f.readline()
        print(f1,end="")

except:
    print("file does not exists")
finally:
    f.close()
    
    
    
    
    
    
    
    
    




