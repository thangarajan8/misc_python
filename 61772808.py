# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:35:54 2020

@author: Thanga
"""
import datetime
l = [27.0, 2.0, 2019.0, 19.0, 59.0, 59.99]
l_int = list(map(int,l))

d = datetime.datetime(l_int[2],l_int[1],l_int[0], l_int[3], l_int[4],l_int[5])
print(d)