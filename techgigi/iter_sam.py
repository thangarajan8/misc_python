# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:39:11 2019

@author: Thangarajan
"""

a = iter(range(0,100))
next(a)

lots_of_fours = [4] * 100_000_00
import sys
sys.getsizeof(lots_of_fours)
it_lots_of_fours = iter(lots_of_fours)
sys.getsizeof(it_lots_of_fours)

