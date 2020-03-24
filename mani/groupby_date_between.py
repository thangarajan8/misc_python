# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:59:38 2020

@author: Thanga
"""

import pandas as pd

df = pd.read_csv('groupby_date_between.csv')

dates =  pd.to_datetime(df.date, format='%m-%d-%y')

df1 = (df.assign(date=dates)
        .groupby(['user_id', pd.Grouper(key='date', freq='3D')])
        .sum()
        .reset_index())


df['amt_add'] = df.assign(date=dates).groupby(['user_id', pd.Grouper(key='date', freq='3D')]).transform('sum')