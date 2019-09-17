# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:40:33 2019

@author: 10541
"""

x = [5,3,1,2,3,3]
sum(x)
sorted(x)
int(len(x)/2) 
[[_,x.count(_)]for _ in x]


from collections import Counter
c=Counter(x)
c.keys()
c.values()
max_count = 0
i = 0
index = 0
for _ in c.items():
    print(_)
    print(_[1])
    if max_count < _[1]:
        max_count = _[1]
        index = i
    i += 1
v = []    
for _ in c.items():
   if _[1] == max_count:
       v.append(_[0])
       
mode = v[0]