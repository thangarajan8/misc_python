# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 22:53:18 2019

@author: Thangarajan
"""

p = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0"""

arr = [list(map(int,a.split(' ')))  for a in   p.split('\n')]
rows = len(arr)
columns = len(arr[0])

for i in range(6):
    for j in range(0,i+3):
        print(i,j)
    print('8888888888')
s = '10.0.0,1'
import re
re.split('. |, ',s)

uid = 'B1CD102354'
pattern = re.compile(r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$')
x = re.match(pattern,uid)
if x:
    print(1)