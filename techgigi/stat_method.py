# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:04:45 2019

@author: Thangarajan
"""

class Calculator:

    # create addNumbers static method
    @staticmethod
    def multiplyNums(x, y):
        return x + y

print('Product:', Calculator.multiplyNums(15, 110))