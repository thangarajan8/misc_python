# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:51:49 2019

@author: Thangarajan
"""
from contextlib import contextmanager

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
with closing(urllib.urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)