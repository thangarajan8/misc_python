# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:25:00 2019

@author: Thanga
"""

a = [10,4,3,5]
n = 4
k = 0
numberOfSwaps = 0
for i in range(n):
    
    for j in range(n-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j+1] ,a[j]
            numberOfSwaps += 1;
            print(a)
        k += 1


sorted(a) == a
