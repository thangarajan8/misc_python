# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:20:51 2019

@author: Thangarajan
"""
import sys

sys.setrecursionlimit = 100000
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = 5000
print(fact(n))