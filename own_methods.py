# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:15:01 2019

@author: Thangarajan
"""

class Name(str):
    def my_method(self):
        return self[0]
    

name = Name('thanga')
name.lower()
name.my_method()

