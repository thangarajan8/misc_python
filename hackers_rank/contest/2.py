# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 23:02:05 2019

@author: 10541
"""

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
l = [1,2,1,2]
n = 3
x = [l[i:i + n] for i in range(0, len(l), n)]
