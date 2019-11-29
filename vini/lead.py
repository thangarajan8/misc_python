# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:31:23 2019

@author: Thanga
"""
def change_pos(df,column_name):
    cur_pos = 0
    pos = []
    rows = []
    for _,row in df.iterrows():
       if row[column_name] > 0:
           cur_pos = row[column_name]
           pos.append(row[column_name])
           row['new_value'] = cur_pos
           rows.append(row)
       else:
           row['new_value'] = cur_pos
           rows.append(row)
           
    df_updated =  pd.DataFrame(rows)
    return df_updated
import pandas as pd
df = pd.read_csv('pos.csv')
df1 = change_pos(df,'value')