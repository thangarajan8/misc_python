# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:18:53 2019

@author: Thangarajan
"""

class Name:
    def __init__(self):
        pass
    def __adder(self,a):
        return a+a


nums = []
while True:
    n = int(input())
    if n != 0:
        nums.append(n)
    else:
        break
    
