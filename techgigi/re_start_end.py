# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:23:03 2019

@author: Thangarajan
"""

import re

s, k = 'aaadaa','aa'
pattern = re.compile(k)
r = pattern.search(s)
if not r: print ("(-1, -1)")
while r:
    print ("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(s,r.start() + 1)