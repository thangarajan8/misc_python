# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:49:00 2019

@author: Thanga
"""
import re
s = '..122345678910111213141516171820212223'

pattern = re.compile(r'([a-zA-Z0-9])\1+')

match = re.search(r'([a-zA-Z0-9])\2+',s)
print(match.groupdict())
match.group(1)
