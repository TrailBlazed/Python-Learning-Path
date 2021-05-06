# -*- coding: utf-8 -*-
"""
Created on Wed May  5 21:26:55 2021

@author: tskir
"""

"""
Ques 8: Write programs to evaluate each of the following equations.
(i) V = u + at. (ii) S = ut+1/2a
(iii) T=2*a+√b+9c (iv) H = √b**2 +p**2 

"""

u=float(input("Enter the value of u:"))
a=float(input("Enter the value of a:"))
t=float(input("Enter the value of t:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
p=float(input("Enter the value of p:"))

V= u +a*t
S=u*t+(0.5**a)
T=2*a+(b**2)+9*c
H=(b**2+p**2)**0.5
print("V:",V)
print("S:",S)
print("T:",T)
print("H:",H)

 
 
 