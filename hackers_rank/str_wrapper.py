# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:58:37 2019

@author: 10541
"""

content = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
width = 4
results = ''
for i in range(0,len(content),width):
    
    result = content[i:i+width]+'\n'
    results = results+result
print(results)    