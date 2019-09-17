# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:15:06 2019

@author: Thangarajan
"""

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
        
class B():
    def func3(self):
        print('func3')
    def func4(self):
        print('func4')

class C(A,B):
    def func5(self):
        print('func5')
    def func6(self):
        print('func6')
        
c = C()
c.func1()
c.func2()
c.func3()
c.func4()
c.func5()
c.func6()