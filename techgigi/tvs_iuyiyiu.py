# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:32:55 2019

@author: Thangarajan
"""

def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 

print(computeGCD(7,3))
