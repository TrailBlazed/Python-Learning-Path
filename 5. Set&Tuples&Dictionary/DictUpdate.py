# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:39:38 2021

@author: tskir
"""

"""Changing Dictionary values"""

DictEx={1:"a",2:"b",3:"c",4:"d"}
print("Using update() function")
DictEx.update({1:"z"})
print(DictEx)
"""Another way of Updation"""
print("Updating other way")
DictEx[2]="y"
print(DictEx)



