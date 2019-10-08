# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:21:52 2019

@author: Thanga
"""

import random
def is_sorted(nums:list):
    for i in  range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

def bogosort(nums:list):
    global counter
    while not is_sorted(nums):
        random.shuffle(nums)
        counter += 1
        print(nums)
    return nums



counter = 0
numbers = [8,7,6,5,5,4,3]
result = bogosort(numbers)