# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:23:33 2022

@author: Pastor
"""

# List
my_list = [1,2,3]
my_list = ['STRING', 100, 2, 3]
len(my_list)

mylist = ['one', 'two', 'three']

mylist[0] # indexing
mylist[1:] # slicing

another_list = ['four', 'five', 'six']

new_list = mylist + another_list

new_list[0] = 'ONE ALL CAPS' # change elements of a list

## Methods

# add
new_list.append('seven') # add items at the end of the list
# remove
new_list.pop() # remove last element of the list
popped_item = new_list.pop() # store the last element of a list

# we can remove specific elements of a list by passing the index to the .pop method
new_list.pop(0) # delete the first element of a list

# how to oder the elements of a list
new_list.sort() # this sort happens inplace, which mean there is no need to store in a variable

# reverse method
num_list = [1,3,4,8]

num_list.reverse() # inplace method
