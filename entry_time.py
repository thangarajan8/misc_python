# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:26:32 2019

@author: Thanga
"""

from datetime import datetime
with open('d:/bin/entry_date.txt','w') as f:
    f.write(str(datetime.now()))