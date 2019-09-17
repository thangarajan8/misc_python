# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:19:46 2019

@author: Thangarajan
"""
def power(x):
    return x*x
import pandas as pd
from functools import reduce

df = pd.read_csv('thanga.csv')

l = list(range(1,11))

l_map = list(map(power,l))
    
# lambda element : operation iter
l_lambda = list(map(lambda x : x*x , l))

# filter (lambda element : cond , iter)
l_filter = list(filter(lambda x: x % 2 == 0, l))


l_reduce = reduce(lambda x,y : x*y ,l*10)


df_loc = df.loc[df['POS']=='CCU']
df_iloc = df.iloc[0,1]

df_first_five_loc = df.iloc[2:5,3:5]



