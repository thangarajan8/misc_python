# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:30:07 2019

@author: Thangarajan
"""

class Parent(object):
    def __init__(self):
        self.value = 5

    def __get_value__(self):
        return self.value

class Child(Parent):
    def get_value(self):
            return self.value+100
c = Child()
print(c.get_value())

