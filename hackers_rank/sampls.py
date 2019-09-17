# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:08:42 2019

@author: 10541
"""



sentence = 'give me the total net sales'.split()
wb = []
n = 6
for N in range(n):
    wb += [sentence[i:i+N] for i in range(len(sentence)-N+1)]

xb = ['_'.join(_) for _ in wb]
yb = [_ for _ in xb if len(_) >0  ]