# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:38:04 2019

@author: Thangarajan
"""
n = int(input())
a = tuple(map(int,input().split())) 
q = int(input())
for i in range(q):
    cnt = sum(map(lambda x: x==int(input()), a))
    if cnt < 1:
        print('NOT PRESENT')
    else:
        print(cnt)
