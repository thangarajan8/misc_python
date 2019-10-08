# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:35:31 2019

@author: Thanga
"""

import timeit

start = timeit.default_timer()

a = list(range(10000000))

del a[0:6]

stop = timeit.default_timer()

print('Time with pop: ', stop - start)  

start = timeit.default_timer()

c = list(range(10000000))

d = c[1:]

stop = timeit.default_timer()

print('Time with slice: ', stop - start)  