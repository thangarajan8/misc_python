# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:33:09 2019

@author: Thangarajan
"""

def divide_chunks(l, n): 
    for i in range(0, len(l), n):  
        yield l[i:i + n]

a = [4, 35, 80, 123, 12345, 44, 8, 5]
k = 10

a = tuple(map(str,a))
lenths = [len(b) for b in a]
max_lenght = max(lenths)
x = list(divide_chunks(a, k)) 
    
sep1 = '+'
cells = '|'
for i in range(k):
    sep1 += '-'*max_lenght+'+'
    cells += ' '*(max_lenght-1)+'%s'+'|'

#print(sep1)
for s in x:
    sep = '+'
    cl = '|'
    for i in s:
        cl += ' '*(max_lenght-len(i))+i+'|'
        sep += '-'*max_lenght+'+'
    
    print(cl)
    print(sep)