# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:25:12 2020

@author: Thanga
"""
import re
with open('sample.txt','r') as f:
    for l in f.readlines():
        match = re.search(r'\d{2}/\d{2}/\d{4}', l)
        if match is not None:
            print(match.group())
