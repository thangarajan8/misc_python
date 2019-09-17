# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 19:01:24 2019

@author: 10541
"""
import time
sample_text = "thanga than working with vini sample truck girl green love"

sample_dict = {"thanga ":"thangarajan","vini":"ammu"}
start_time = time.time()
#for k in range(10000):
#    temp_text = None
#    for i in sample_dict.keys():
#        print(i,sample_dict.get(i))
#        temp_text = sample_text.replace(i,sample_dict.get(i))
#        sample_text = temp_text
dict_keys = list(sample_dict.keys())
for i in range(1000000):
    for word in sample_text.split(' '):
        if word in dict_keys:
            sample_text = sample_text.replace(word, sample_dict.get(word))
end_time = time.time()
print(sample_text)
print(end_time-start_time)

import pandas as pd
df =pd.read_csv('no_header.csv',header=None)
for _,row in df.iterrows():
    print(row[0])
    
print(lower('SAM'))
print('SAM'.lower())
