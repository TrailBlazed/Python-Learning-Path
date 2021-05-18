# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:02:12 2021

@author: tskir
"""

"""Loop and Join Sets"""
s={"a","b","c"}
#looping
print("loop for set s:")
for i in s:
    print(i)
    
    
"""Join Sets"""
q={"x","y","z","a","b"}

#union
g=s.union(q)
print("Union - present in both set s and q")
print(g)
print("Intersection - present in both set s and q")
h=s.intersection(q)
print(h)
print("Symeetric Difference - Elements present in  both set s and in q")
w=s.symmetric_difference(q)
print(w)



  
  
