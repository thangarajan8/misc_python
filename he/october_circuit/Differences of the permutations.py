# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:49:34 2019

@author: Thanga
"""
def calc(n):
    per = permutations(range(1,n+1))
    while True:
        try:
            yield reduce(lambda x,y : x+y ,map(lambda x: n - x, next(per)))
        except StopIteration:
            break
        
        

from itertools import permutations
from functools import reduce
n = 4
c = calc(n)
res = 0
while True:
    try:
       res += next(c)
    except StopIteration:
        break




