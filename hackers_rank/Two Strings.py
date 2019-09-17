# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:27:47 2019

@author: Thangarajan
"""

def twoStrings(s1,s2):
    d = {}
    for i in s1:
        d[i] = i
    for j in s2:
        if d.get(j,False):
            return True
            break
    return False
s1 = 'hello'
s2 = 'world'
print(twoStrings(s1,s2))