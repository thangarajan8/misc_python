# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:38:20 2019

@author: Thangarajan
"""

def binary(arr,l,r,search_element):
    
    mid = int(l + (r - l)/2)
    
    if arr[mid] == search_element:
        return mid
    if arr[mid] > search_element:
        print('First Half')
        print(arr[:mid])
        return binary(arr,l,mid-1,search_element)
    else:
        print('Second Half')
        print(arr[mid:])
        return binary(arr,mid+1,r,search_element)
    
    
    return -1

arr = list(range(10))
search_element = 5

result = binary(arr,0,len(arr)-1,search_element)

print(result)