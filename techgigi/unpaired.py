# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:01:10 2019

@author: Thangarajan
"""


from collections import Counter
A = [9,3,9,3,9,7,9]
c = dict(Counter(A))
odds = None
for key in c.keys():
    if c[key] == 1:
        odds=key

