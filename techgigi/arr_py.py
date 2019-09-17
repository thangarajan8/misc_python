# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:35:50 2019

@author: Thangarajan
"""

import array
arr = array.array('i', [1, 2, 3])  

for i in range(3):
    print(arr[i])
    
arr.append(4)
