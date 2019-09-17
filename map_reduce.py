# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:09:57 2019

@author: Thangarajan
"""

x = lambda x : x*x
y = lambda y : y>2
a = [1,2,3,4,5]
b = [(i,i*i) for i in range(5)]
for i in map(x,a):
    print(i)

for i in filter(y,a):
    print(i)