# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:04:08 2018

@author: 10541
"""

def split_df_by_columns(ip_df,col_name):
    try:
        unique_values = ip_df[col_name].unique()
        print(unique_values)
        dfs = []
        for value in unique_values:
            print(site_name)
            df = ri_loc_df[ri_loc_df[col_name]==value]
            dfs.append(df)
        return dfs
    except KeyError:
        logger.error('Given column is {} not present in Dataframe'.format(col_name))
        
    
    

import pandas as pd
from logzero import logger
file_path = 'E:\\RD\\smap\\RI_LOC.csv'
ri_loc_df=pd.read_csv(file_path) ## reading file using file path
logger.info(ri_loc_df.head(n=10)) # get top 10 rows
logger.info(ri_loc_df.tail(n=10)) # get bottom 10 rows
ri_loc_df.dtypes ## datatyoe of object
type(ri_loc_df.dtypes) # dataype of what we have printed
ri_loc_df.columns
type(ri_loc_df.columns)
column_list=list(ri_loc_df.columns)
print("The DataFrame contains {} number of columns".format(len(column_list)))

site_names = ri_loc_df["site_name"]

ri_loc_df['site_name'].unique()

unique_site_name = site_names.unique()
dfs = []
for site_name in unique_site_name:
    print(site_name)
    df = ri_loc_df[ri_loc_df.site_name==site_name]
    dfs.append(df)



df1 = split_df_by_columns(col_name='site_name',ip_df=ri_loc_df)


