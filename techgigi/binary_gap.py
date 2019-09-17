# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 22:47:53 2019

@author: Thangarajan
"""

num = 66561
binary_num = bin(num)[2:]
binary_num.count('1')
import re
X = [m.start() for m in re.finditer('1', binary_num)]
total = []

for i in range(len(X)-1):
    total.append( X[i+1]-X[i]-1    )

         