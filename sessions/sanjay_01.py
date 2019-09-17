# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:09:49 2019

@author: 10541
"""

#1
a  = 10
a **= 10

b = 123432
b %= 10000

#2 
a = [1,2,3]
a and a

def my_and(a,b):
    if  bool(a) == False:
        return a
    else:
        return b

x = [1,2,3]
y = []

x and y
[] and ()
my_and(x,y)
my_and(y,x)


l1 = list(range(0,5000000))

