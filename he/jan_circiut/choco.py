# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:19:44 2020

@author: Thanga
"""

c = 13
n = 5

def get_rem(c,n):
    prev_sum = 0
    cby2 = c/2
    if (cby2*(cby2+1))/2 > c:
        c1 = int(c/2)
    for i in range(1,c1+1):
        total = 0
        for j in range(i,i+n):
            total += j
        print(total,c)
        if total > c:
            break
        prev_sum = total
    if prev_sum == 0 :
        return c
    else:
        return c - prev_sum
    
print(get_rem(20,3))
    
a,b = map(int,'1 2'.split(' '))

c = 3
int((c*(c+1))/2)
cby2 = c/3
(cby2*(cby2+1))/2 
