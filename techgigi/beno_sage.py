# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:28:40 2019

@author: Thangarajan
"""

s = 'AABCAAADA'
n = 3
words = []
for i in range(1,n+1):
    k = (i-1)*n
    words.append(s[k:i*n])

for word in words:
    d = {}
    for char in list(word):
        d[char] = None
    print(''.join(d.keys()))
    
