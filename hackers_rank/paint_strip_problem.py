# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:11:06 2019

@author: 10541
"""
y = []
word_l = ['WBR','RBW']
for i in word_l:
    nsp = 4
    x = i*int(nsp/3)
    len(x)
    if len(x) != 4:
        if x[-1] == 'R':
            x = x+'W'
        elif x[-1] == 'W':
            x = x+'R'
        
    y.append(x)
len(y)*2
