# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:31:58 2022

@author: Pastor
"""

#inheritance

class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def who_am_I(self):
        
        print("I am an animal")
        
    def eat(self):
        print("I am eating")
        
        


class Dog(Animal):
    
    def __init__(self):
        
        Animal.__init__(self)
        print("Dog created!")
        
    def bark(self):
        print("WOOF!")
        

my_dog = Dog()

## polimorphism

class Dog():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + "says woof!"
    
        
class Cat():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + "says meau!"      
        
        
        
class Animal():
    def __init__(self,name):
        self.name = name
        
    def speak():
        raise NotImplementedError("Subclass must be implement this abstract method")
        
class Dog(Animal):
    
    def speak(self):
        return self.name + " says woof!"
    
class Cat(Animal):
    
    def speak(self):
        return self.name + " says meow!"
    
    
fido = Dog("Fido")

isis = Cat("Isis")

fido.speak()

isis.speak()    
    
    
    
        
        
        
    
    

