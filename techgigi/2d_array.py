# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:22:44 2019

@author: Thangarajan
"""

data = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0"""

arr = [i.split(' ') for i in data.split('\n')]

for i in range(len(arr)):
    for j in range(len(arr)):
        print(i,j)
        print(arr[i][j])
#    print()