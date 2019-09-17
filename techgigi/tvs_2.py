# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:28:59 2019

@author: Thangarajan
"""

a = [(j**2)*10**(2-i) for (i,j) in enumerate(range(1,4))]
print(sum(a))


a = 4
b= '8.678'
c = -5
s = '{0:.4f} {2} {1}'.format(a,b,c)
print(s)