# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:11:38 2019

@author: 10541
"""

list(range(10,0,-1))
for i in range(10,0,-1) : print(i)
for i in range(10,0,):
    print(i)

for i in range(,,):
    print(i)
    
l = [1,2,3]

if 2 in l:
    print(l.index(2))
    
    
for i in True:
    print(1)
    
for i in  range(1.1,3,0.1):
    print(i)
    
for i in range(1,10,0):
    print(i)
    
for i in range(,10,):
    print(i)
    
def elenext(l):
    for i in l:
        yield i
        
c = elenext(l)
next(c)


while (1,2):
    print(1)