# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 12:23:03 2019

@author: Thangarajan
"""
def knot(X,n,m,Y):

    x = 0
    o = 0
    hor_lines = []
    for i in range(n):
        line = ''
        for j in range(m):
            line += X[i][j]
            hor_lines.append(line)
            
    diag_lines = [''.join([X[y-x][x] for x in range(n) if 0<=y-x<n]) for y in range(2*n-1)]
    
    [row[0] for row in X]
    ver_lines = []
    for i in range(n):
        line =''
        for j in range(3):
            line += X[j][i]
            ver_lines.append(line)
    result = diag_lines+hor_lines+ver_lines
    for i in result:
        if i.count('x') == Y:
            x += 1
        elif i.count('o') == Y:
            o += 1
    print(x,o)

n = 3
m = 3
X = [
['x', 'x', 'x'],
['x', 'o' ,'x'],
['x', 'x', 'x']
]
knot(X,n,m,3)
