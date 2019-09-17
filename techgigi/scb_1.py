# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:34:07 2019

@author: Thangarajan
"""

name = 'hacker book'
import re
v_count = 0
for word in name.split(' '):
    pattern = re.compile('(a|e|i|o|u)')
    if len(pattern.findall(name)) % 2 == 0:
        v_count += 2
    else:
        v_count += 1

