# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:15:48 2019
Jumping on the Clouds

https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
@author: Thanga
"""

c = list(map(int,'0 0 0 0 1 0'.split(' ')))
#x = list(map(int,'0 0 1 0 0 1 0'.split(' ')))
n  = len(c)
step_count = 0
flag = True
for i in range(n-1):
    if c[i+1] == 0 and not flag:
        step_count += 1
        flag = True
    else:
        flag = False
