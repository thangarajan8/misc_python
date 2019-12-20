# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:38:48 2019

@author: Thanga
"""

import pandas as pd

df = pd.read_csv('wrong_dates.csv', dtype=str)

df['c1'] = df.apply(lambda x : x['dateproceed'].split('.')[0],axis=1)

df['c2'] = df.apply(lambda x : len(x['c1']), axis=1)

