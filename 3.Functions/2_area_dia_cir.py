# -*- coding: utf-8 -*-
"""
Created on Thu May 13 15:47:16 2021

@author: tskir
"""

"""Ques 2.Find diameter, circumference and area of circle """
import math

def circle(r):
    d=2*r
    a=r*r
    c=2*math.pi*r
    print("diameter = {} ,area={}, cirference={}".format(d,a,c))

r=int(input("Enter the radius"))
circle(r)
