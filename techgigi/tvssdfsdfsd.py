# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:03:45 2019

@author: Thangarajan
"""

def divisors(num):
    X = []
    for x in range (2, num+1):
        if (num % x) == 0:
            X.append(x)
    return X

a = [4,1,3,2]
n = 6
[i for i in range(2,n+1) if n % i == 0]
for i in range(len(a)-1):
    f = a[i]
    s = a[i+1]
    f_d = set(divisors(f))
    s_d = set(divisors(s))
    coms = f_d&s_d
    if len(coms) == 0:
        if (f/s) > (s/f):
            if f > s :
                
                print(i)
            else:
                print(i)
