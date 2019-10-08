# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:31:54 2019

@author: Thanga
"""

s = "fdhlvosfpafhalll"
counter = 0
if len(s) % 2 == 0:
    fh = s[: int(len(s) / 2)]
    sh = s[int(len(s) / 2) :]
    d = {}

    for i in sh:
        d[i] = None
    for i in fh:
        if i not in d.keys():
            counter += 1

else:
    counter = -1
