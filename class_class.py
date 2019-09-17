# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:54:35 2019

@author: Thangarajan
"""

class Student:
    def __init__(self):
        print('The student class was called')
        self.sum = 100
    def add(self,a,b):
        return a+b
    def __sum(self,a,b):
        return a+b+b

class Class(Student):
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b+10
class Session(object):
    def __init__(self):
        pass
    
s = Student()
c = Class()
s.add(2,3)
c.add(4,5)

class AddMe(str):
    def __init__(self,name):
        self.name = name
    def get_one(self,name):
        return self.name[0]
name = 'thanga'
name.lower()
