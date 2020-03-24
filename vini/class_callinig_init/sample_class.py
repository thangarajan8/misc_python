# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:10:58 2020

@author: Thanga
"""

localConfig = 0
class Sample(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(a,b)
        


def adder():
    global localConfig
    localConfig += 100
    Sample(1,2)