# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:57:06 2019

@author: 10541
"""

def minion_game(string):
    name_list = []
    f_list = []
    for i in string:
        name_list.append(i)
    stuart = []
    kevin  = []
    vowels = ['A','E','I','O','U']
    for N in range(len(string)+1): 
        x = [name_list[i:i+N] for i in range(len(name_list)-N+1)]
        for y in x:
            if len(y) > 0:
                word = ''.join(y)
                f_list.append(word)
                if word[0] in vowels:
                    kevin.append(word)
                else:
                    stuart.append(word)
    if len(stuart) > len(kevin):
        print('Stuart', len(stuart))
    else:
        print('Kevin', len(kevin))

minion_game('THANGARAJAN')