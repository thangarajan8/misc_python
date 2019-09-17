# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:50:27 2019

@author: Thangarajan
"""

a = [5,4,3,2,1]
a_len = len(a)

for i in range(a_len):
    
    for j in range(a_len-i-1):
        print(a[j],a[j+1])
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]