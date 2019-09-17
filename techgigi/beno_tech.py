# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 01:37:33 2019

@author: Thangarajan
"""

a = list(range(1,101))
b = [ True if i % 2 ==0 else False   for i in a]

b = [i for i in a if i %2 == 0]

d = {'a':1,'a':8}
d['a']
