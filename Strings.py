# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:12:38 2022

@author: Pastor
"""

mystring = "Hello world"

mystring[-3]


mystring[:5] # up to but not including

# middle of the string
mystring = "abcdefgh"
mystring[3:6]

# get every two elements string
mystring[::2] # step size

mystring[2:7:2] # start:end:step_size

# Write your string index below
# Start with 'Hello World'
# and make sure to match spaces and capitalization exactly
"Hello World"[8]

## Inmutability of the string

# Strings are not mutable! (meaning you can't use indexing to change individual elements of a string)
name = "Sam"

# name[0] = 'P'

# The aboove line won't work so we need to work around to change from Sam to Pam
# first store the last letters of the string into a different variable
# them assing append the letter 'P' to the new variable

last_letters = name[1:]

'P' + last_letters


# string concatenation
letter = 'z'
letter *10

x = "Hellow world"
x.upper()
x.split('o')


# Formating with the .format() method

print('This is a string {}'.format('INSERTED'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))

print('The {f} {b} {q}'.format(f='fox', b='brown', q='quick'))

# float fomating follows "{value:width.precision f}"
result = 100/777

print("The result was {r:1.3f}".format(r=result))

# Use the f format

name = "Jose"

print(f'Hello, his name is {name}')

name = "Sam"
age = 3

print(f'{name} is {age} years old')



















