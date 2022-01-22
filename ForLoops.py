# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 23:00:22 2022

@author: Pastor
"""

# iteration: perform a action over the object 
# you can iterate over every character in a string, iterate over every item in a list,
# iterate over every key of the dictionary

# syntax
my_iterable = [1,2,3]

for item_name in my_iterable:
    print(item_name)
    
    
# example:
mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)
    
    
# print just even number

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd number: {num}")
        
list_sum = 0

for num in mylist:
    list_sum = list_sum + num
    
print(list_sum)
        

# iterating over string

for char in "Hello world":
    print(char)


for _ in "Hello world": # if you are not using the var you are iterating
    print("Cool!")

# iterate over tuple
tup = (1,2,3)


mylist_tup = [(1,2), (3,4), (5,6)]

len(mylist_tup)

# tuple unpacking
for a, b in mylist_tup:
    print(b)
    print(a)


# dictionary
d = {'k1':1, 'k2':2, 'k3':3}


# by default the dictionary iterate over the keys
for item in d:
    print(item)

# iterate over dictionary over the values
for key, value in d.items():
    print(key)
    print(value)

# iterate over the values
for value in d.values():
    print(value)
    
    