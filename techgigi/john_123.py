# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:53:17 2019

@author: Thangarajan
"""

sent = 'i am campus mind. am in campus mind'
flag = False
cur = ''
next_word = ''
words = []
for l in sent:
    if l == ' ':
        words.append(cur)
        if cur == 'campus':
            print(next_word)
            cur = ''
            next_word = ''
            flag = True            
        cur = ''
        flag = False
    elif not flag:
        cur += l
    else:
        next_word += l
    print(next_word)
    