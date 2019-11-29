# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:04:08 2019

@author: Thanga
"""
import re
code_string = """
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""

x = re.sub(' && ','and',code_string)