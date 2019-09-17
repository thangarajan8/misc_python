# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:08:56 2019

@author: Thangarajan
"""

r_count = 4
arr = [1,2,3,4,5]
for i in range(4):
    first = arr[0]
    arr.append(first)
    del arr[0]

    print(arr)
