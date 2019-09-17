# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:29:43 2019

@author: Thangarajan
"""

A = [1,2,3,4,5,6,324,435,324,543]

K = 7

def solution(A:list, K):
    # write your code in Python 3.6\    
    for i in range(K):
        A.insert(0,A.pop())
        print(A)
    return A


solution(A,K)