# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:54:39 2019

@author: Thanga
"""
try:
    import unittest
except ModuleNotFoundError:
    import unittest2


class TestSum(unittest.TestCase):
    """
    This is sample doc string
    """

    def test_sum(self):
        """
        test the sum of list is equal to 6
        """
        self.assertEqual(sum([1, 2, 13]), 6, "Should be 6")

    def text_sum_tuple(self):
        """
        test the sum of the tuple is equal to 10
        """
        self.assertEqual(sum((1, 2, 31, 4, 5)), 10, "Should be 6")


unittest.main()
