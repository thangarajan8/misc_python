# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:45:11 2019

@author: 10541
"""
import operator
x = {}
for i in range(int(input())):
    dummy = input()
    works = list(map(int,input().split()))
    for work in works:
        x[work]=bin(work).count('1')
print(x)
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)
dict(sorted_x)
