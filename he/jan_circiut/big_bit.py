# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:11:06 2020

@author: Thanga
"""

b = 1
tc = int(input())
for t in range(tc):
    a = int(input())
    bin_a = bin(a)[2:]
    bin_a_length = len(bin_a)-1
    for i in range(0,a):
        x = (b*(2**i))-1 

        bin_x = bin(x)[2:]
        bin_x_length = len(bin_x)
        if bin_x_length == bin_a_length:
            print(i,bin_x,x)
          
        

len(bin(255)[2:])
len(bin(345)[2:])
