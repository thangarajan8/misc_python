# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:19:17 2019

@author: Thangarajan
"""
text = 'thangarajan'
sufs  = []
prefs = []
for i in range(1,len(text)):
    sufs.append(text[i:])
    prefs.append(text[:i])
    
    
class Sample:
    def __init__(self):
        return 1
    
f = None

for i in range(5):
    with open('bin_iter.py','r') as f:
        if i == 2:
            break
print(f.closed)
    
import re
sent = 'a b c'
matched = re.match(r'(.*) (.*?) (.*)',sent)
print(matched.group(2))
i = 5
while True:
    if i % 0011  == 0:
        break
    print(i)
    i += 1