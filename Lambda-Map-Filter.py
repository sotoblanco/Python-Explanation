# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 22:06:57 2022

@author: Pastor
"""

# Lambda expressions, map and filter

def square(num):
    return num **2

my_num = [1,2,3,4,5]

# calculate the square for each item of the list

for num in my_num:
    sq = square(num)
    print(sq)
    
map(square, my_num)

for item in map(square, my_num):
    print(item)
    
list(map(square, my_num))    
    

## filter

def check_even(num):
    return num%2 == 0

mynums =[1,2,3,4,5]

list(filter(check_even, mynums))

for i in filter(check_even, mynums):
    print(i)

# lambda expressions

def square(num):
    result = num**2
    return result

def square(num):
    return num**2

def square(num): return num**2

lambda num: num**2

list(map(lambda num: num**2, mynums))

list(filter(lambda num: num%2 == 0, mynums))

names = ["Andy", "Eve", "Sally"]

list(map(lambda x:x[::-1], names))




























