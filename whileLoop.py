# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:13:19 2022

@author: Pastor
"""

# while loops in python

# while the condition is true the block of code will continue running

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    
    x += 1
    

# break, continue, pass

# pass key word: does nothing at all but allow to run the code without errors

x = [1,2,3]

for item in x:
    pass

# continue: continues run the code (goes to the top of the closest enclosing loop)
mystring = "Sammy"

for letter in mystring:
    if letter == "a":
        continue
    print(letter)
    
# break: breaks out of the current closest enclosing loop
for letter in mystring:
    if letter == "a":
        break
    print(letter)

# let's use while with the break statement
x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
    
    
for i in range(0,10):
    if i == 5:
        break
    print(i)
    
    if i == 2:
        print(f"second loop {i}")







    
    