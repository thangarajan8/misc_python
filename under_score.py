# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:33:11 2018

@author: 10541
"""

import time
start_time = time.time()
j = 0
for i in range(0,100000000):
    j +=i
    
print(' Total Time {}'.format(time.time()-start_time))
j = 0
start_time = time.time()
for _ in range(0,100000000):
    j += _
print(' Total Time {}'.format(time.time()-start_time))