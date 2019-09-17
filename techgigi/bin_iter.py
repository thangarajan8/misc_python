# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 23:23:35 2019

@author: Thangarajan
"""

def binary(arr,start,end,search_element):
    itr = 1
    while len(arr) > 1:
        print(' Iter : {}'.format(itr))
        mid = int(start+(end-1)/2)
        mid_value = arr[mid]
        if  mid_value == search_element:
            return mid
        elif mid_value < search_element:
            arr = arr[mid:]
        else:
            arr = arr[:mid]
        return -1

arr = list(range(10))
search_element = 8

result = binary(arr,0,len(arr)-1,search_element)

print(result)
print(arr[result])