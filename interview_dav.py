# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:40:09 2019

@author: Thanga
"""

a =  [0,0,0,1,1,1,1,2,2,2,3,3,3]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

for i in range(len(a)-1):
    if a[i] != a[i+1]:
        print(b[i+1])