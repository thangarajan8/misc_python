# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:38:19 2019

@author: Thanga
"""

#conda install -c conda-forge boto3
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

n = 10
for i in range(n,1,-1):
    if n % i == 0 :
        print(i)
        if isPrime(i):
            print(i)
        break
            
            
isPrime(10**12)

