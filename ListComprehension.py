# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:05:44 2022

@author: Pastor
"""

# List comprehension

mystring = "Hello"

mylist = []
for letter in mystring:
    mylist.append(letter)
    
# this is a equivalent method that allow to save space in the code
mylist = [letter for letter in mystring]

mylist = [num for num in range(0,11)]

# if you want to get just even numbers

mylist = [x**2 for x in range(0, 11) if x%2==0]

celcius = [0, 10, 20, 34.5]

fahrenheit = [((9/5)*temp + 32 ) for temp in celcius]

# if else can be use in list comprehension but it would be more difficult to understand

# nested loop

mylist = []

for x in [2,4,6]:
    for y in [1, 10, 1000]:
        mylist.append(x*y)

# gives the same results in just one line of code but it is more difficult to understand        
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]






