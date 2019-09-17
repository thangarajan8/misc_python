# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:00:31 2019

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
        
a = A()
b = B()
b.func1()
b.func2()
b.func3()
b.func4()