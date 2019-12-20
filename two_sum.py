# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:47:50 2019

@author: Thanga
"""

class Solution:
    def twoSum(self, nums, target: int) :
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]+nums[j] == target and i!=j:
                    return [i,j]
        
s = Solution()
s.twoSum([3,2,4],6)
