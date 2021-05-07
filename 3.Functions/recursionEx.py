# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:24:42 2021

@author: tskir
"""

"""Print 1-n numbers"""

def tennumbers(x):
    if(x==0):          #base case
        return
    if(x):             #recursion
        tennumbers(x-1)
    print(x)

x=10
tennumbers(x)


