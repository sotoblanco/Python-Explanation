# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:42:52 2022

@author: Pastor
"""
# reverse string
phrase = "I am home"

list_text = phrase.split()

out = []

for i in range(1, len(phrase.split())+1):
    
    
    out.append(list_text[-i])
    
    string_list = " ".join(out)


nums = [1, 2, 3, 3]

for i in range(len(nums)):
    
    if (nums[i] == 3) and (nums[i-1] == 3):
        print("done", i)
        break
    
    
    
    
    
    if i == 0:
        
        if (nums[0] == 3) and (nums[1] == 3):
            print(i)
    
    else:
        if (nums[i] == 3 and nums[i-1] == 3) and (nums[i-1] == 3 and nums[i] == 3):
            print(i, i+1, i - 1)
    
    
    
    print(i, i-1)
    
    
