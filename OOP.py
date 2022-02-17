# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:27:09 2022

@author: Pastor

OOP in Python
"""

class Dog():
    
    species = "mammal"
    
    def __init__(self, breed, name, spots):
        
        # attributes
        # we take in the argumentx
        # assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots
        
    def bark(self,number):
        
        print("WOOF! my name is {} and the number is {}".format(self.name, number))
        
    
my_dog = Dog(breed = "Lab", name = "Sammy", spots=False)

my_dog.breed
my_dog.name
my_dog.spots

my_dog.bark(3)


class Circle():
    
    pi = 3.14
    
    #class object attribute
    
    def __init__(self, radius=1):
        
        self.radius = radius
        self.area = radius * radius*Circle.pi
        
    # method
    def get_circunference(self):
        
        return self.radius * self.pi * 2
    
    
my_circle = Circle(30)
    
my_circle.get_circunference()
    
    
    

