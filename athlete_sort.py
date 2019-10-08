# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:51:15 2019

@author: Thanga
"""

row,col = 5,3
data = ['10 2 5','7 1 0','9 9 9','1 23 12','6 5 9']
sort_index = 1

d = {}
for i in range(5):
    d[i] = list(map(int,data[i].split(' ')))
    
v = sorted(d.items(), key= lambda x : int(x[1][sort_index]))

for i in v:
    print(' '.join( [str(x) for x in i[1]]))