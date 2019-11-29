# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 16:41:09 2019
https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem
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
def prime_sum(n,prev_sum=None,prev_num=None):
    if not prev_sum:
        prime_sum = 0
        for i in range(1,n+1):
            if isPrime(i):
                prime_sum += i
        return prime_sum
    else:
        prime_sum = prev_sum
        for i in range(prev_num+1,n+1):
            if isPrime(i):
                prime_sum += i
        return prime_sum
    
a = [5,10]
temp = 0
for n in a:
    if temp == 0:
        psum = prime_sum(n)
        temp = n
    else:
        psum = prime_sum(n,prev_sum=psum,prev_num=temp)
        temp = n
    print(n,psum)