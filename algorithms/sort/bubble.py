# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:05:15 2020

@author: Thanga
"""
a = [64, 34, 25, 12, 22, 11, 90]*10000
swap_counter = 0
it= 0
n = 1
for j in range(len(a)-1):
    for i in range(len(a)-j-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
        it += 1
   