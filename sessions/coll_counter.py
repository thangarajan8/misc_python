# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 15:31:38 2019

@author: Thangarajan
"""
from collections import Counter
c =['sathish','sathish','beno','jow']

d = dict(Counter(c))
keys = d.keys()
values = list(set(d.values()))
second_max = values[-2]

names = []
for _ in d.keys():
    if second_max == d.get(_):
        names.append(_)
        
print(sorted(names)[0])
