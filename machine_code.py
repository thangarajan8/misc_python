# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:58:29 2019

@author: Thanga
"""

def add(a,b):
    return a+b

def add_temp(a,b):
    c = a+b
    return c

import dis

dis.dis(add)
dis.dis(add_temp)
