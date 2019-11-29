# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:15:44 2019

@author: Thanga
"""

from string import ascii_lowercase

ascii_dict = dict(zip(ascii_lowercase,map(ord,ascii_lowercase)))

d = dict(zip(ascii_lowercase,range(10)))
