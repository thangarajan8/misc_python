# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:17:50 2019

@author: Thangarajan
"""

class A:
    def func1(self):
        print('func1')
    def func2(self):
        print('func2')
        
class B(A):
    def func3(self):
        print('func3')
    def func4(self):
        print('func4')

class C(B):
    def func3(self):
        print('func5')
    def func6(self):
        print('func6')
        
c = C()
c.func3()