# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:10:36 2019

@author: 10541
"""

cols = 10+20+20
rows = cols * 3
mid = int((rows - 3) / 2)
sym1 = 'T'
sym2 = '.V.'
title = '@@THANGA WEDS VINI@@'
title_length = len(title)
title_position = int((rows - title_length) / 2)
half_mid_pos = int(cols/2)
half_mid_neg = int(cols/2)+2
for i in range(1,cols,1):
#    print(mid)
#    if i % 2 != 0:
    sym2_count = int((rows-(mid*2))/3 )
#    print(sym2_count)
    print(sym1*mid+sym2*sym2_count+sym1*mid)
    mid = int(mid -3)
    
    if i == half_mid_pos:
        print(sym1*title_position+title+sym1*title_position)
        break
mid = int((rows - 3) / 2)
for i in range(cols-1,0,-1):
    sym2_count = abs(int((mid*2) ))-3
    sym2_count = int(sym2_count/3)
    _mid = int((rows - (sym2_count*3) )/2)
    print(sym1*_mid+sym2*sym2_count+sym1*_mid)
#    print(_mid,sym2_count,_mid)
    mid = mid - 3
    if i == half_mid_neg-1:
        break