# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 22:04:17 2019

@author: Thangarajan
"""

word = 'AAABBB'
r_count = 0
for i in range(len(word)-1):
    if word[i] == word[i+1]:
        r_count += 1