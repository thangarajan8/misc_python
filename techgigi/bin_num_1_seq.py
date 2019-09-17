# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:26:57 2019

@author: Thangarajan
"""

n = 5
n_bin = bin(n)[2:]

seq = 0
seqs = set()
for c in n_bin:
    if c == '1':
        seq += 1
    elif c == '0':
        seqs.add(seq)
        seq = 0
seqs.add(seq)
print(max(seqs))