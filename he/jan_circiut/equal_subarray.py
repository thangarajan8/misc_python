# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:11:41 2020

@author: Thanga
"""

arr = [1, 4, 9, 3, 6]
k = 9
n = 5
max_len = 0
iters = 0
        
def get_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])
for i in range(2,n):
    for x in get_ngrams(arr,i):
        max_x = max(x)
        incr = 0
        for j in x:
            incr += max_x - j
            iters += 1
            if incr > k:
                break
        if incr <= k:
            if max_len < i:
                max_len = i
