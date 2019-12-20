# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:36:57 2019

@author: Thanga
"""

from math import pow
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        neg_flag = False
        if x < 0:
            neg_flag = True
            x = -(x)
        while x != 0 :
            remainder = x % 10
            rev = (rev * 10) + remainder
            x //= 10
        if neg_flag:
            if rev > pow(2,31)-1:
                return 0
            return -rev
        else:
            if rev > pow(2,31)-1:
                return 0
            return rev