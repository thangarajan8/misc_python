# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:30:51 2019

@author: Thangarajan
"""
l = []
for i in range(10):
    try:
        l.append(int(input()))
    except ValueError:
        print('not valid')
        pass
    
    
import string
a = list(string.ascii_uppercase)
try:
    b = a[100]
    c = int(a[2])
except ValueError:
    print('ValueError')   
except IndexError:
    pass
    print('IndexError')
    pass
    
##
Exception
class AgeError(Exception):
    def __init__(self):
        Exception.__init__(self,"Age must be greater that 18") 
    

raise AgeError
age = 10
if age >= 18:
    print('Valid')
else:
    raise AgeError
    
from urllib import requests
