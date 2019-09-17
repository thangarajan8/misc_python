# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:30:50 2018

@author: 10541
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
filename = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'
columns = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


df = pd.read_csv(filename, names = columns)
print("Done")

df.head()
df.replace("?", np.nan, inplace = True)

missing_data = df.isnull()
data = df.notnull()

avg_1 = df["normalized-losses"].astype("float").mean(axis = 0)
df["normalized-losses"].replace(np.nan, avg_1, inplace = True)

avg_2=df['bore'].astype('float').mean(axis=0)
df['bore'].replace(np.nan, avg_2, inplace= True)

df.dtypes
df['price'] = df['price'].astype('int')
df['price'].replace(np.nan,0,inplace=True)

price_avg = df['price'].astype('float').mean(axis=0)

df['price'].replace(0,price_avg,inplace=True)

df['length'].max()
df['length'].min()
df['length'].std()

df['length_norm'] = df['length']/df['length'].max()
df['length_norm_min_max'] = (df['length']/df['length'].min())/(df['length'].max()-df['length'].min())
df['lenght_zscore'] = (df['length']-df['length'].mean())/df['length'].std()
min_price = int(min(df['price']))
max_price = int(max(df['price']))
binwidth =  int(max_price-min_price/4)
bins = range(min_price,max_price,binwidth)
group_names = ['Low', 'Medium', 'High']
df['price_binned'] = pd.cut(df['price'],bins,labels=group_names)
