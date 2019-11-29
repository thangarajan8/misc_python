# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:59:00 2019

@author: Thanga
"""
word = 'zoo'
word_dict = {}
for w in list(word):
    if w in word_dict.keys():
        word_dict[w] = word_dict[w]+1
    else:
        word_dict[w] = 1
        