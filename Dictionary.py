# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:47:27 2022

@author: Pastor
"""

# Useful when you want to associated keys to values
my_dict = {'key1': 'value1', 'key2':'vale2'}
my_dict['key1']

# you can assign any type of variable you want:
d = {'k1': 123, 'k2':[0,1,2],'k3':{'insidekey':100}}

d['k2'][2]

d = {'key1':["a", "b", "c"]}
d['key1'][2].upper()

d = {'key1':100, 'key2':200}

# add a key and value to the dictionaire
d['key3'] = 300

# change values
d['key1'] = "NEW VALUE"

# see the keys
d.keys()

# see the values
d.values()

# see the pair
d.items()


