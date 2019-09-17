# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:25:58 2019

@author: Thangarajan
"""

def linear(arr,element,length):
    
    for i in range(0,length):
        if element == arr[i]:
            return i
    return -1

arr = [1,23,4,5,3,2,4]
length = len(arr)
element = 3
print(linear(arr,element,length))