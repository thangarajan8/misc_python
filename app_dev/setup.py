# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:38:22 2020

@author: Thanga
"""

from distutils.core import setup
import py2exe

setup(
    windows=[{'script': 'foobar.py'}],
)