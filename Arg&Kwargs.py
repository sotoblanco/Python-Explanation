# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 11:31:26 2022

@author: Pastor
"""

# *args and **kwards

def myfunc(a, b):
    
    return sum((a,b)) * 0.05

myfunc(40,60)    

# *args return a tupple
def myfunc(*args):
    print(args)
    
myfunc(40, 60, 100)

# **kwargs return a dictionary

def myfunc(**kwargs):
     if 'fruit' in kwargs:
         print(f'My fruit of choice is {kwargs["fruit"]}')
     else:
        print('I did not find any fruit here')
        
myfunc(fruit = "Apple", veggie = "letuce")


# we need to follow the same order, so first define the args and them the kwargs when you
# call the function

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs["food"]))
          
myfunc(10, 20, 30, fruit = "orange", food= "eggs", animal = "dog")         
          


def myfunc(*args):
    list_args = [i for i in args if i %2 == 0]
    return list_args
          
myfunc(5,6,7,8) 


def myfunc(x):
    out = []
    
    for i in range(len(x)):
        if i%2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
            
    return "".join(out)
      
myfunc("asdhsdada")    
        
      
        