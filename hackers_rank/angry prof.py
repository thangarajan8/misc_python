# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:36:28 2019
https://www.hackerrank.com/challenges/angry-professor/problem
@author: Thanga
"""

def angry_prof():
    late_or_not = lambda i : 1 if i <= 0 else 0
    
    k = [-1 ,-3 ,4,2]
    a = 3
    if len(list(filter(late_or_not, k))) < a :
        return 'YES'
    else:
        return 'NO'

