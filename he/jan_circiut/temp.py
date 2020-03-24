# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:53:17 2020

@author: Thanga
"""
c = 6
for i in range(c):
    x = int((i*(i+1))/2)
    if x > c:
        i = i-1
        result = int((i*(i+1))/2)
        break