# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 18:30:01 2019

@author: 10541
"""
total_ants = 3
total_pos= total_ants*2
p  = total_ants/total_pos
q = total_ants / total_pos
print(p+q)
p*pow(q,-1) % pow(10,9)+7
from fractions import Fraction
x = Fraction(p)
x*pow(x,-1) % pow(10,9)+7
