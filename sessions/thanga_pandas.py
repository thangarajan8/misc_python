# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:20:31 2019

@author: Thangarajan
"""

import pandas as pd
import calendar
from datetime import datetime
df = pd.read_csv(r'E:\Projects\RI\ri.csv')

#1
df_first_50 = df.head(5000)
df_last_50 = df.tail(50)
concated_df = pd.concat([df_first_50,df_last_50]*10)

#2


df['month'] =  pd.to_datetime(df['RECEIPT_MONTH_YEAR'], format='%Y%m').month
df['month_1'] = df['month'].dt.month
df['Month'] = df['month_1'].apply(lambda x: calendar.month_abbr[x])

df['nvm'] = df['RECEIPT_MONTH_YEAR'].apply(lambda x : calendar.month_name[int(str(x)[-2:])])

#3
X = df_last_50.stack([0,1])
df.reset_index(level=df_last_50.columns) 

#4

df_first_50['cat_first'] = df['TradeSubCategory'].apply(lambda x : x.split('&')[0] if '&' in x  else x)

#5
nulls = df_first_50['CarpetArea'].isna().sum()
df_first_50['CarpetArea'].fillna((df_first_50['CarpetArea'].mean()), inplace=True)

#6
df_first_50['PortFolioName_cat'] = df_first_50['PortFolioName'].astype('category')
cats ={}
for i,term in enumerate(set(df_first_50['PortFolioName'].tolist())):
    cats[term] = i 
df_first_50['port_cat'] = df_first_50['PortFolioName'].apply(lambda x : cats[x])

#7