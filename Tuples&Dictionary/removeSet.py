# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:08:42 2021

@author: tskir
"""

"""Remove and Delete set"""
s={1,2,3,4}

print("Original Set")

#remove 2 from set
s.remove(2)
print("Remove an element 2 from set")
print(s) 

#another way to remove item is discard
print("Discard element 3 from set")
s.discard(3)
print(s)

#clear  the set from all elements
print("Clear the set s")
s.clear()
print(s)

#delete the set s

print("Delete the set s")
del s
print("done deleting")


