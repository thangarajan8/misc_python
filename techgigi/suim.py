# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 13:33:44 2019

@author: Thangarajan
"""

from collections import Counter
s = 'baac'
k = 2
X = dict(Counter(list(s)))
for key in X.keys():
    if X[key] == k:
        print(key)
        s = s.replace(str(key),'')
        break
        