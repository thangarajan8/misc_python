# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:47:48 2019

https://www.hackerrank.com/contests/projecteuler/challenges/euler016/problem
@author: Thanga
"""
"""
Testing

int(2**2000//10)

for i in range(10):
    print(2**i)
    
"""



def sum_num(n):
    result = 0
    while n != 0:
        result += n % 10
        n = int(n//10)
    return result
        
n = int(input())

for _ in range(n):
    print(sum_num(2**int(input())))
    
    
