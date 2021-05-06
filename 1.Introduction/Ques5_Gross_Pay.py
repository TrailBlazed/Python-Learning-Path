# -*- coding: utf-8 -*-
"""
Created on Wed May  5 20:51:49 2021

@author: tskir
"""

"""Ques 5:Gross pay( without considering overtime)"""

hours=float(input("Enter the number of hours:"))
wage=float(input("Enter the hourly wage:"))
gross=wage*hours
print("Gross pay:%0.2f" %gross)