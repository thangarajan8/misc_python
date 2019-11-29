# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:51:50 2019

@author: Thanga
"""

import re
pos_rom = 'IVXLCDM'
ip = 'DXXVIIII'
if re.match(r'^[{}]*$'.format(pos_rom),ip):
    print('hai')
else:
    print('Bye')