# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 16:14:46 2019

@author: Thanga

https://stackoverflow.com/questions/58387731/plotting-month-year-as-x-ticks-in-matplotlib
"""
from string import ascii_lowercase

d = {x:x.upper() for x in ascii_lowercase}

name = 'stackoverflow'

sentence = "can't do it"

d = {"can't": "can not"}

res = ' '.join([d.get(i, i) for i in sentence.split()])