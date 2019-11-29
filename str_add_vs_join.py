# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:43:53 2019

@author: Thanga
"""

from time import time

i = 10000000
stime = time()
str1 = ''
for i in range(i):
    str1 += 'a'
print('Total Processing time {}'.format(time()-stime))

stime = time()
str_list = []
app = str_list.append
for i in range(i):
    app('a')
str2 = ''.join(str_list)
print('Total Processing time {}'.format(time()-stime))