# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 23:13:29 2019

@author: 10541
"""
import string
x = ['bubby',
'bunny',
'berry']
max_n = 5 * len(x)
c = 'zzzzz'

def get_diff_score(i,j):
    cnt = 0
    for k in range(len(i)):
        if i[k] != j[k]: 
            cnt += 1
    return cnt
total = 0
while not max_n == total:
    total = 0
    for _ in x:
        total += get_diff_score(_,c)

