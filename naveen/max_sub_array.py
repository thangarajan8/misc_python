# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:26:26 2019

@author: Thangarajan
"""

def sliceList(alist,n):
    s_list = []
    for i in range(0,len(alist),1):
        if len(alist[i:i+n]) == n:
            s_list.append(alist[i:i+n])
    return s_list
a = [1,-1,1,2,3,-5]

maximum_sum = 0
max_sub = []
for i in range(len(a)):
    sub_list = sliceList(a,i)
    for _ in sub_list:
        sum_sub_list = sum(_)
        if maximum_sum < sum_sub_list:
            maximum_sum = sum_sub_list
            max_sub = _
                