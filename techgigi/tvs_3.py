# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:31:58 2019

@author: Thangarajan
"""

def func(a,b):
    if b == 0 :
        return a
    else:
        return func(a ^b , (a&b) << 1)
    
func(5,6)
