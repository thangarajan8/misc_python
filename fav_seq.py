# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:47:09 2019

@author: Thanga
"""

from string import ascii_lowercase
test_string = 'abcabc'
d = { i:ord(i) for i in ascii_lowercase}
test_dict = dict(zip(test_string,map(ord,test_string)))
