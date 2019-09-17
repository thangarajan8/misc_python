# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:26:06 2019

@author: Thangarajan
"""

class c (Exception):
    pass
b =1000
try:
     b /= b
     raise c()
except c:
    print('A')
else:
    print('B')
    
try:
    b = b/5
except Exception:
    print('C')
else:
    print('D')