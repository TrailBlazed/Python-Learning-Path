# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:49:01 2021

@author: tskir
"""

""" Accessing Items in Dictionary """
dictEx={1:"a",2:"b",3:"c",4:"d"}
i=dictEx[1]
print("Value of the key 1 is: {}".format(i))

"""Another way of Accessing Items in Dictionary"""
j=dictEx.get(1)
print("Another way to get value for key 1 is:{}".format(j))


""" Access the keys"""
k=dictEx.keys()
print(k)


