# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:47:19 2019

@author: Thangarajan
"""

import itertools

l = list('1222311')

for _ in itertools.groupby(l):
    print(_,_[0])
