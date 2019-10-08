# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:30:53 2019

@author: Thanga
"""

import unittest

#assert sum([1,2,6-3,4]) == 10 , "should be 10"

def test_total(number_list):
    assert sum(number_list) == 6 , "Should be 10"
    
number_list = [0,1,2,3,0,0,0,0,0,0,0]
test_total(number_list)
print('All test passed')

