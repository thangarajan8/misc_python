# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:07:48 2019

@author: Thangarajan
"""

a = [9,8,7,6,5,4,3,2,1]

for i in range(len(a)):
    min_index = i
    
    for j in range(i+1,len(a)):
        if a[min_index] > a[j]:
            min_index = j
    a[i],a[min_index] = a[min_index],a[i]
print(a)