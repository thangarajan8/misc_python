# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:06:04 2019

@author: 10541
"""

from itertools import combinations

word = 'HRISBAD'
count =  6
result = []
terms = sorted([ _ for _ in word])
for i in range(2,count+1):
    print(i)
    x = [''.join(sorted(_)) for _ in list(combinations(word,i))]
    result += sorted(x)
print('\n'.join(terms))
print('\n'.join(result))
