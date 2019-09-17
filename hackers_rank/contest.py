# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:37:41 2019

@author: 10541
"""

pile = [1,2,3,4,5,5]
max_coin = max(pile)
p = []
for i in range(0,len(pile)):
    if pile[i] != max_coin:
        p.append(pile[i])
print(max(p))
list1 = pile
max=max(list1[0],list1[1]) 
secondmax=min(list1[0],list1[1]) 

import heapq
heapq.nlargest(2,pile)
