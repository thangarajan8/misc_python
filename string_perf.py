# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:28:29 2019

@author: Thanga
"""

from timeit import timeit
from string import ascii_lowercase

lower_list = list(ascii_lowercase*1000)

def make_string():
    mkstring = ''
    for i in lower_list:
        mkstring += i
    return mkstring

def join_string():
    return ''.join(lower_list)
print('String concat 1000 :',timeit(make_string, number=1000))

print('String join  1000 :',timeit(join_string, number=1000))