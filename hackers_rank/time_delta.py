# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:48:44 2019

@author: 10541
"""
from datetime import datetime as dt
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    t1 = dt.strptime(t1,fmt)
    t2 = dt.strptime(t2,fmt)
    diff = (t1-t2).total_seconds()
    abs_diff = abs(diff)
    int_diff = int(abs_diff)
    return int_diff
    
    
inputs = """Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000""".split('\n')

time_delta(inputs[2],inputs[3])
