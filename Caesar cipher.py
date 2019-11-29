# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:34:29 2019

@author: Thanga
"""

from string import ascii_uppercase

test_cases = 1
shift = 0
for tast_case in range(test_cases):
    a,b = 'ADDME'.upper(),'UNDEF'.upper()
    d = dict(zip(ascii_uppercase,range(1,27)))
    diff = []
    for k,v in zip(a,b):
        print(d[k],d[v])
        _diff =  d.get(v)-d.get(k)
        if _diff < 0 :
            diff.append(26+_diff)
        else:
            diff.append(_diff)
    print(diff)
    if shift % len(a) == 0:
        print(shift/len(a))
    else:
        print(-1)
    