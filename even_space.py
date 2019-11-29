# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:22:19 2019

@author: Thanga
"""

strings = ["All", "happy", "families", "are", "alike", "every", "unhappy", "family", "is", "unhappy", "in", "its", "own", "way"]

width = 30


counter = 0
spaced_list = []
temp_str = []
for i in range(len(strings)-1):
    counter += len(strings[i])+1
    
    temp_str.append(strings[i])
    if counter+len(strings[i+1])>= width:
        spaced_list.append(temp_str)
        print(counter)
        counter = 0
        temp_str = []
temp_str.append(strings[-1])
spaced_list.append(temp_str)
cnt = 0
for s in spaced_list:
    