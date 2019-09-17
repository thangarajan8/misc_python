# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:49:51 2019

@author: 10541
"""
import string 
from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
perm = permutations(list(string.ascii_lowercase)) 
# Print the obtained permutations 
for i in list(perm): 
    print(i)