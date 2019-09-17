# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:01:31 2019

@author: Thangarajan
"""

import itertools
n = [i for i in range(1,int(input())+1)]
values = list(input())
set_size = int(input())
inc,a =0,0
for j in itertools.combinations(n,set_size):
    vals = [values[i] for i in  j]
    # i -= 1
    # j -= 1
    inc += 1
    if 'a' in vals:
        a += 1
        print(vals)
print(a/inc)
    
