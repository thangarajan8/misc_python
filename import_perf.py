# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:40:16 2019

@author: Thanga
"""
from timeit import timeit

def import_inside():
#    import str
    str.lower('Sample')
    
#import str

    
def dont_import():
    'Sample'.lower()

print('Import Inside',timeit(import_inside, number=1000000))
print('No Import',timeit(dont_import, number=1000000))