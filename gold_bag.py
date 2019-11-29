# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:45:53 2019

@author: Thanga
https://www.hackerearth.com/challenges/competitive/mock-online-coding-assessments-easy-python/problems/933213680dc04e7ea5867576a8305a86/
"""

from itertools import combinations
a_list = [2, 4, 2, 3, 1]
a_list = sorted(a_list)
com = combinations(a_list,3)
max_nums = sum(map(max,com))
#total = 0
#
#flag = True
#while flag:
#    try:
#        total += next(com)[-1]
#    except StopIteration:
#        flag = False
    
