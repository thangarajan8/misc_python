# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:14:16 2019

@author: Thangarajan
"""

a = [3,1,2,4,3]
asum = 0
arsum =sum(a)
for i in range(len(a)-1):
    asum += a[i]
    minus = abs(arsum-asum)
    v = abs(asum-minus)
    print(v)
    if mins > v:
        mins = v