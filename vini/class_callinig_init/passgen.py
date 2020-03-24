# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:44:39 2020

@author: Thanga
"""

import string
class PassGen(object):
    def __init__(self,n):
        self.lcase = string.ascii_lowercase.split()
        self.ucase = string.ascii_uppercase.split()
        self.n = n
    def alpha_pass(self):
        
        