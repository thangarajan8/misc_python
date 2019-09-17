# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 12:49:42 2018

@author: 10541
"""
import time
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
n_df=pd.DataFrame()
df_l = []
i = 100000
start_time = time.time()
for i in range(0,i):
    n_df = pd.concat((n_df,df),axis=0)
print('Total time for concat {}'.format(time.time()-start_time))    

start_time = time.time()
for i in range(0,i):
    df_l.append(df)
df = pd.concat(df_l)    
print('Total time for concat list of dataframes {}'.format(time.time()-start_time))    