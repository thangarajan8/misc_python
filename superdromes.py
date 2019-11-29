# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:49:54 2019

@author: Thanga
"""

b = list(map(int,input().split()))

for i in b:
    x = bin(i).replace('0b','')
    if x == x[::-1]:
        print(x)