# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:09:41 2019

@author: 10541
"""


from collections import Counter
word = 'abc'
d = dict(Counter(word))
flag= False
for i in d.keys():
    if d.get(i) == 1 or d.get(i) == 2:
        flag = True
    elif d.get(i) > 2:
        print(len(word[:-1]))

if flag:
    print(0)