# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:37:20 2019

@author: 10541
"""
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))

