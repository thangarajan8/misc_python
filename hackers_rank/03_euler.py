# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:27:12 2019

@author: 10541
"""

import math
for i in range(int(math.sqrt(1000000000000000)),1,-1):
    if 600851475143 % i ==0:
        flag = False
        for y in range(int(math.sqrt(i)),1,-1):
            if(i % y ==0):
               flag = True
        if(flag!=True):
            print(i)
            break
def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
   
    return True
is_prime(3)


i = [1,2,3]
c = False
[c= True for _ in i if _ < 0 else c = False]
