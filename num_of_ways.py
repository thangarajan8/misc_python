# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:11:50 2019

@author: Thanga
"""
import copy
dis = 3
step = 2
steps = dict.fromkeys((range(1,step+1)))

for i in range(1,step+1):
    temp = copy.deepcopy(dis)
    print(temp,'dsffs')
    pos = set()
    while temp > 1:
        bal = temp - i
        print(bal,steps,temp)
        if bal in steps:
            pos.add(True)
        else:
            pos.add(False)
        temp -= 1
    print(pos)
    
  
    
