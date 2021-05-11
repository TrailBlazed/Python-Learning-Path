# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:08:35 2021

@author: tskir
"""
"""List as an Array"""
x1 = ['a', 'b', 'c']

x1.append('d')
print("x1 after append()=",x1)   #Adds an element at the end of the list"""

x2=['w','x']
x1.clear() #Removes all the elements from the list
print("x1 after clear()=",x1)

x3=[]
x3=x2.copy() #Returns a copy of the list
print("x3 after copy()=",x3)

print("count of w in x3 =",x3.count('w')) #Returns the number of elements with the specified value

x4=('g','h')   #declaring tuple
x3.extend(x4) #Add the elements of a list (or any iterable), to the end of the current list
print("x3 after extend() with a tuple x4 =",x3)

r=x3.index('x')
print("Index of x in x3:",r) #Returns the index of the first element with the specified value

q='e'
x3.insert(1,q) #Adds an element at the specified position
print("x3 after insert() at position 1=",x3)

x3.pop(2)
print("x3 after pop() at index 2:",x3) #Removes the element at the specified position

x3.remove('w')
print("x3 after remove() for value w:",x3) #Removes the first item with the specified value

x3.reverse()
print("Reverse of list x3:",x3) #Reverses the order of the list

x3.sort()
print("Sort the list x3:",x3) #Sorts the list

