# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:06:45 2022

@author: Pastor
"""

class Book():
    
    def __init__(self, title, author, pages):
        
        self.title = title
        self.author = author
        self.pages = pages
        
        
    def __str__(self): # special method for str and print in general
        
        return f'{self.title} by {self.author}'
    
    def __len__(self): # most used method str and len
        
        return self.pages
    
    def __del__(self):
        
        print("A book object has been deleted")
    
    
b = Book("Python Rocks", "Jose", 200)

print(b)

len(b)

# delete variables from your memory using del

del b



