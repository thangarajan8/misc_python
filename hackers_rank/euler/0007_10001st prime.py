# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:06:52 2019
https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem
@author: Thanga
"""

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
x = []
for i in range((10**5)+1):
    if isPrime(i):
        x.append(i)
        
prime_dict = dict(zip(range(1,len(x)+1),x))
