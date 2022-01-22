# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:28:38 2022

@author: Pastor
"""

# useful operators in python

mylist = [1,2,3]

for num in range(0,10,2):
    print(num)
    

list(range(0,11,2))


index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    
    index_count += 1
    

# often we make those type of operation when we want to see the index count
index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1
    
# enumerate allow to see the index of the loop and store in a tuple for which you can use the unpacking that we already discuss
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# zip function: allow to match list of the same length in a tupple object
# if the list are the same length it would use the shortest one as reference
#zip together list
mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100,200,300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

list(zip(mylist1, mylist2))

# in key word
# check if a is in the string

'a' in 'a word'
# check if the key is in the dictionary

'mykey' in {'mykey':345}

d = {'key':345}

345 in d.values()

from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9]

# inplace function to shuffle a list
shuffle(mylist)

from random import randint
randint(0,10)

results = int(input('Enter a number: '))

