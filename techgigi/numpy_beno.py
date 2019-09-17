# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:23:39 2019

@author: Thangarajan
"""

import numpy as np
n_array = np.array(
       [ [0,1,2],
        [3,4,0],
        [9,0,4]], dtype=np.float32)

col_mean = np.mean(n_array, axis=0)

X = np.where(np.equal(n_array, 0), col_mean, n_array)


Y = list(map(int,'1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'.split()))
from collections import Counter
c = dict(Counter(Y))
room_no = 0
for key in c.keys():
    if c[key] == 1:
        room_no = key
        break
myset = set(Y)
k = 5
print(((sum(myset)*k)-(sum(Y)))//(k-1))

