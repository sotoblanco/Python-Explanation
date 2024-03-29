## Introduction to python

# Type of variables

# Integer
a = 5

# Float
b = 5.0

# String
c = "Hello"

mystring = "Hello world"
mystring[0]

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
num_list.reverse()





# concatanate list


#### Physics in python
high_market = 15827.75
low_market = 15570
distance =  high_market - low_market
time = 30
velocity = round(distance/time,2)
time_day = time * 13.5

print(f'Points per minute {velocity}')

# If we keept the average velocity what would be the distance traveled at the market close
distance_traveled_day = velocity * time_day

print(f'Distance the full day {distance_traveled_day}')
