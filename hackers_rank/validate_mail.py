# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:16:15 2019

@author: Thanga
"""
def check_ext(ext):
    if re.search(r'^\w+([\.-]?\w+)*@\w+\d*(\.\w{2,3})+$',ext):
        return True
    else:
        return False
import re

mails = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

#re.match(r'([a-zA-Z0-9])',mails[0].split('@'))

check_ext('rase23@ha_ch.com')
