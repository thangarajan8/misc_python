# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:27:36 2019

@author: Thangarajan
"""

df1 = df[['Site_Code','CarpetArea']]
df_grp = df1.groupby(['Site_Code'], as_index=False).mean()
df1.describe(include='all')
import pandas as pd
pd.get_dummies(df['Site_Code'])
