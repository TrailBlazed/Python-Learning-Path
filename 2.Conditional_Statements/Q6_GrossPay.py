# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:05:17 2021

@author: tskir
"""

"""Q6:Gross Salary calculator (consider overtime)"""

h=float(input("Number of hours worked:"))
hourlyPay=float(input("Hourly Pay"))
if(h>40):
    sal=40*hourlyPay+(h-40)*(hourlyPay*1.5)
    
else:
    sal=40*hourlyPay
    
print("Gross pay for %3.2f hours is:" %sal)

