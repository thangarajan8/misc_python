# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:06:06 2019

@author: 10541
"""

text = 'AABCAAADA'
n=3
for _ in [text[i:i+n] for i in range(0, len(text), n)]:
    temp_l  = []
    for i in  _:
        temp_l.append(i)
    temp_l = ''.join(list(set(temp_l)))
    print(temp_l)
