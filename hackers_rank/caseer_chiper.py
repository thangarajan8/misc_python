# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:10:12 2019

https://www.hackerrank.com/challenges/caesar-cipher-1/problem

@author: Thanga
"""

from string import ascii_lowercase as lc
from string import ascii_uppercase as uc
k = 4
s = 'Hello_World!'
ld = dict(zip(range(27),lc))
ud = dict(zip(range(27),uc))

res = []
e_result = 'Lipps_Asvph!'
for i in s:
    if i.islower():
        i_value = lc.find(i)
        i_shift = i_value + k
        
        if i_shift > 26:
            res.append(ld.get(i_shift%26))
        else:
            res.append(ld.get(i_shift))
    elif i.isupper():
        i_value = uc.find(i)
        i_shift = i_value + k
        if i_shift >= 26:
            res.append(ud.get(i_shift%26))
        else:
            res.append(ud.get(i_shift))
    else:
        res.append(i)

result = ''.join(res)