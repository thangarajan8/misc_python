# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:32:30 2019
https://www.hackerrank.com/challenges/reduced-string/problem
@author: Thanga
"""

s = 'aaabccddd'
strs = []
for i in range(len(s)-1):
    print(s[i],s[i+1])
    if s[i] != s[i+1] and s[i] ==s[i-1]:
        strs.append(s[i])
        
if strs:
    print(''.join(strs))
else:
    print('Empty String')