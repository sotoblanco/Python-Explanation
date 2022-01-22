# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:52:36 2022

@author: Pastor
"""

myfile = open('myfile.txt') # open the file

#pwd # working directory

myfile.read()

myfile.seek(0)

myfile.readlines()

myfile.close()

with open("myfile.txt") as my_new_file:
    contents = my_new_file.read()
   
# Open

x = open("test.txt", "w")
x.write("Hello World")
x.close()

