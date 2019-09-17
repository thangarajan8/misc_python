# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:58:09 2019

@author: 10541
"""
phi = 1.618033989
n = 1000
import math
int(math.pow(phi,n)/math.sqrt(5))

curr_num = 2
curr_num = int(math.pow(((1 + math.pow(5 , 0.5)) / 2),10) * curr_num + 0.5)


s = 0
big = 2
pre = 0
while big < 10:
    n_e = big*4 + pre 
    s += big
    pre = big
    big = n_e
print(s)