# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:03:10 2019

@author: Thanga
"""
from collections import Counter
s = 'abcdabcd'
f,l = 2,7
s1 = s[f-1:l]
d = {}
for i in s1:
    if i in d:
        val = d[i]
        d[i] = val+1
    else:
        d[i] = 0

counter = dict(Counter(s))
