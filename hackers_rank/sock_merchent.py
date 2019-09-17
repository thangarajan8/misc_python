# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:36:56 2019

@author: 10541
"""
from collections import Counter
l = [int(_) for _ in '10 20 20 10 10 30 50 10 20'.split()]
cnt = Counter(l)
match_pairs = 0
for i in cnt.items():
    match_pairs += int(i[1]/2)