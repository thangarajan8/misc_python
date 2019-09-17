# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:08:57 2019

@author: Thangarajan
"""

import pandas as pd
df = pd.read_csv('vini.csv')

idx = df.groupby(['Trade Category','Site_Code'])['Trading Density'].transform(max) == df['Trading Density']
result = df[idx]

df2 = pd.read_csv('vini_prop.csv')

df2["max_value"] = df2[["p0", "p1","p2","p3"]].max(axis=1)
