# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:40:40 2019

@author: 10541
"""

#l = [i for i in range(10) if i % 3 == 0 or i % 5 == 0]


    
    
n = 100000000000000000000000
a = (n - 1) // 3
b = (n - 1) // 5
d = (n - 1) // 15
c = 3 * a * (a + 1)//2 + 5 * b * (b + 1)//2 - 15 * d * (d + 1)//2
