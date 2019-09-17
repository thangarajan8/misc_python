# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:41:55 2019

@author: Thangarajan
"""

s = 'bcxz'
askey = [ord(i) for i in s]
askey_reversed = askey[::-1]
askey_cmpd = [abs(i-j) for i,j in zip(askey,askey_reversed)]

k = [abs(askey_reversed[i] - askey_reversed[i+1]) for i in range(0,len(askey_reversed)-1)]
j = [abs(askey[i] - askey[i+1]) for i in range(0,len(askey)-1)]
print(k)
print(j)   