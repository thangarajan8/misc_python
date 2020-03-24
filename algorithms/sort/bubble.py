# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:05:15 2020

@author: Thanga
"""
a = [5, 1, 4, 2, 8]
iters = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        x,y = a[i],a[j+1]
        print(x,y)
        iters += 1
        
#        print (a[i] > a[j+1])
        if a[i] > a[j+1]:
            a[i],a[j+1] = y,x
#            a[i],a[j] = x, y
        print(a)