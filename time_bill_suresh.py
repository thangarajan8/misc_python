# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 18:59:08 2018

@author: 10541
"""

a = [1,2,4,10,12,13,14]

b = min(a)
c = max(a)

time = [10,20,40,50,60,70,80]


dummy_bill = list(range(b,c+1))
complete_time = []
find_index = None
for i in range(0,len(dummy_bill)):
    if dummy_bill[i]  in a:
        print('index {}'.format(a.index(dummy_bill[i])))
        complete_time.append(time[a.index(dummy_bill[i])])
        find_index = a.index(dummy_bill[i])
    else:
        print(i)
        print(time[find_index])
        complete_time.append(time[find_index])
