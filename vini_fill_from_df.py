# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:22:20 2019

@author: Thangarajan
"""



import pandas as pd

df1 = pd.DataFrame([
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ],columns =['a','b','c'])

df2 = pd.DataFrame([
        [1,2,0],
        [4,0,6],
        [0,8,0]
        ],columns =['a','b','c'])

df3 = df2.replace(0,pd.np.NaN)

df3[df3.isnull()] = df1

