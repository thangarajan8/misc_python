# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:16:27 2019

@author: Thangarajan
"""

a = [3,1,2]
a = [5,1,2,3,4]

rotate = 0
for i in range(len(a)-1):
    f = a[i]
    s = a[i+1]
    if a[i] < a[i+1]:
        a[i] = f
        a[i+1] = s
    else:
        a[i] = s
        a[i+1] = f
        rotate += 1