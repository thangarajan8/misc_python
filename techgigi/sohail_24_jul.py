# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:22:46 2019

@author: Thangarajan
"""

import numpy as np
np.random.random((3,3,3))

a = [1,2,7,8,6,5,3,10,-9,-10]
min_a = min(a)
max_a  = max(a)
a =set(a)
b = set(list(range(min_a,max_a)))
b-a
import os
a = []
df['fpath'] = df.apply(lambda x : os.path.join(df['Path'],df['source'],df['filename']),axis=1)
for index,rows in df.iterrows():
#    print(rows['filename'])  
   if os.path.isfile(rows['Full_filename '].strip().replace(' .','.')):
       a.append(rows['Full_filename '])