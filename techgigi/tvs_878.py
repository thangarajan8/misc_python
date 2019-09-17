# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:33:03 2019

@author: Thangarajan
"""
def distance(v1, v2):
    return np.sqrt(np.sum((v1 - v2) ** 2))    
import numpy as np

a = np.array([4,3,2,0])
b = np.array([5,2,3,1])
distance(a,b)

import csv
import requests
url = 'http://winterolympicsmedals.com/medals.csv'
r = requests.get(url)
text = list(r.iter_lines())
header = tuple(text[0].decode("utf-8") .split(','))
data = []
for d in text[1:]:
    dat = tuple(d.decode("utf-8").split(','))
    data.append(dict(zip(header,dat)))