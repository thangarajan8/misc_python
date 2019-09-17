# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:43:19 2019

@author: 10541
"""

from collections import OrderedDict

odict = OrderedDict()
odict['a'] = 1
odict['a'] = 2
if 'a' in odict.keys():
    old_value = odict
    
    
s = '12abcd 405'
result = ''.join([i for i in s if not i.isdigit()])
