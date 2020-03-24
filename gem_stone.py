# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:32:11 2020
https://www.hackerrank.com/challenges/gem-stones/problem
@author: Thanga
"""

arr = """abcdde,baccd,eeabg""".split(',')
arr_dict = {}
gems = []
counter = 0
for a in arr:
    temp_dict = {}
    for c in a:
        temp_dict[c] = 1
        
    for b in temp_dict.keys():
        if b in arr_dict.keys():
            b_value = arr_dict[b]
            arr_dict[b] = b_value+1
        else:
            arr_dict[b] = 1
    
for key,value in arr_dict.items():
    if value == len(arr):
        counter += 1