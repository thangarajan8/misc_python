# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:42:01 2019

@author: Thangarajan
"""

A = [ [1, 1, 1, 1], 
    [2, 2, 2, 2], 
    [3, 3, 3, 3], 
    [4, 4, 4, 4]] 

#A = [ [1, 1, 1, 1], 
#    [2, 2, 2, 2], 
#    [3, 3, 3, 3]] 

N = len(A[0])
M = len(A)
B = [[0 for x in range(N)] for y in range(M)]  
for i in range(N):
    for j in range(M):
        B[j][i] = A[j][i]
    