# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:58:39 2019

@author: Thanga
"""


import time
from datetime import datetime, timedelta
print(str(datetime.now() - timedelta(hours=8, minutes = 30))[11:19])
time.sleep(10)
print()