# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:50:08 2019

@author: Thangarajan
"""

import pandas as pd


df = pd.read_csv('data.csv')

salary = 400

df['valid'] = df.apply(lambda x : eval(x['condtion']),axis=1)
