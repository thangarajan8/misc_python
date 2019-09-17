# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 12:51:24 2019

@author: Thangarajan
"""

class A:
   def f1(self):
       print("1")
class B():
   def f1(self):
       print("2")
       
class C(B,A):
   pass


AB = C()
AB.f1()

C.__mro__
C.mro()


class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

M.mro()
X.mro()
A.mro()
M.mro()
M.__mro__
