# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:23:39 2019

@author: Thangarajan
"""

a = [5,4,3,2,1]

for i in range(1,len(a)):
     key = a[i]
     j = i-1
     
     while j >=0 and key < a[j]:
         print(j,key)
         a[j+1] = a[j]
         j -= 1
     a[j+1] = key
