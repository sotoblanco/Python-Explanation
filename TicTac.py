# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 13:20:14 2022

@author: Pastor
"""

# display information

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
    
    
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]


display(row1, row2, row3)

row2[1] = "X"


# user input by default is a string

position_index = int(input("Enter a value"))

def user_choice():
    
    # variables
    
    # initial
    
    choice = "WRONG"
    acceptable_range = range(0,10)
    within_range = False
    
    # two conditions to check
    # digit or within range == false
    
    while choice.isdigit() == False:
        
        choice = input("Please enter a number (0-10): ")
        
        # digit check
        if choice.isdigit() == False:
            print("Sorry that is not a digit")
            
        # range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range == False
            else:
                print()
         
         
    return int(choice)
 
