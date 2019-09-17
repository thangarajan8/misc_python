# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:11:01 2019

@author: Thangarajan
"""

path = 'Ab3bd'
mid_char_pos = int(len(path)/2)
mid_char = path[mid_char_pos]

first_half = path[:mid_char_pos]
second_half = path[mid_char_pos+1:]

first_set = set(first_half)
second_set = set(second_half)


print(len(first_set^second_set))

