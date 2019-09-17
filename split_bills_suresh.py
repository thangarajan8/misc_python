# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:20:47 2018

@author: 10541
"""
from random import randint
import pandas as pd
bills = []

seq = ['a','b','c','d']
for s in seq:
    for i in range(0,randint(10,20)):
        bills.append(s+'_{}'.format(i))
        
static_item = []
for i in bills:
    dummy_l = []
    for j in i:
        if not j.isalnum():
            print(i.find(j))
            ind = i.find(j)
            dummy_l.append(i[:ind])
            dummy_l.append(j)
            dummy_l.append(i[ind+1:len(i)])
            static_item.append(dummy_l)
        

df = pd.DataFrame(static_item)

unique_static = list(set(df[0].tolist()))

dfs = []

for i in unique_static:
    dfs.append(df.loc[df[0] == i])