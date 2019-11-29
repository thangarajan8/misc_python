# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:13:40 2019

@author: Thanga
"""

import unittest
from calc import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)
        
    def test_list_str(self):
        data =['1','2']
        result = sum(data)
        self.assertRaises(result,TypeError)
        
        
if __name__ == '__main__':
    unittest.main()