# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:45:06 2019

@author: Thanga
"""
N = 10**6
isprime = dict(zip(range(1,N),[True]*N))
isprime[0] = isprime[1] = False
for i in range(4, N):
    isprime[i] = False
for i in range(3, N, 2):
    if isprime[i]:
        for j in range(i*i, N, 2*i):
            isprime[j] = False
    
