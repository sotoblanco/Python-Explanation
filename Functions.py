# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:54:27 2022

@author: Pastor
"""

# Functions in Python

def name_of_function(name):
    
    '''
    
    
    '''
    print("Hello " + name)
    

def add_function(num1, num2):
    
    return num1 + num2

result = add_function(3, 6)


name_of_function("Pastor")

def say_hello(name = "Default"):

    print(f'Hello {name}')

# print just to display the results

# if we want to store into a variable you need to use return

# you can use print and return in the same function althoug is not common

def sum_var(a, b):
    print(a+b)
    return a + b

sum_var(10,20)

# returns boolean expression 
def even_check(number):
    return number % 2 == 0

even_check(20)

# return true if any number is even inside a list

def check_even_list(num_list):
    
    # return all even numbers
    
    even_numbers = []
    

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers



check_even_list([1,3,5])

# multiple values return from a function using tupple unpacking

stock_prices = [('APPL', 200), ('GOOGL', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item)

for ticker, prices in stock_prices:
    print(ticker)

# check how an increase of 10 % looks like

for ticker, prices in stock_prices:
    print(prices + prices*0.1)


work_hours = [("Abby", 100), ("Billy", 4000), ("Cassie", 800)]

def employee_check(work_hours):
    
    current_max = 0
    employee_of_month = ""
    
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
            
        else:
            pass
    return (employee_of_month, current_max)


# tupple unpacking from a function using tupple
name, hours = employee_check(work_hours)


# interaction between python functions
example = [1,2,3,4,5,6,7]

from random import shuffle

# this is made inplace so we cannot save into a variable
shuffle(example)

example

# to make it save into a new variable we do:

def shuffle_list(mylist):
    
    shuffle(mylist)
    return mylist


results = shuffle_list(example)

results

mylist = ["", "0", ""]

shuffle(mylist)

def player_guess():
    
    guess = ""
    
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number: 0,1, or 2: ")
        
    return int(guess)
        
        
    
player_guess()


myindex = player_guess()

def check_guess(mylist, guess):
    
    if mylist[guess] == "0":
        print("Correct!")
        
    else:
        print("Wrong gues!")
        
        print(mylist)


mylist = ["", "0", ""]

mixedup_list = shuffle_list(mylist)

guess = player_guess()

check_guess(mixedup_list, guess)





