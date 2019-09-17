# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:57:31 2018

@author: 10541
"""

import pandas as pd
file_path = 'E:\\RD\\smap\\RI_LOC.csv'
ri_loc_df=pd.read_csv(file_path)
ri_loc_df_dup=pd.read_csv(file_path)
a = [[1,'Thanga',100], [2,'rajan',200],[3,'Ammu',300]]
type(a)

a.append([4,'Baby',400])


for _ in a:
    print('EID  : {}'.format(_[0]) )
    print('Name  : {}'.format(_[1]) )
    print('Salary  : {} \n '.format(_[2]) )

ri_loc_df.columns

ri_loc_df['sub_cat_count']

sub2= ri_loc_df['sub_cat_count'] +10

ri_loc_df['sub2']=ri_loc_df['sub_cat_count'] +10

ri_loc_df['sub3'] = ri_loc_df.apply(lambda a: a['sub2']+10, axis=1)

ri_loc_df['sub4'] = ri_loc_df.apply(lambda b: b['sub2'] + b['sub3'], axis=1)

ri_loc_df_dup['sub2'] = ri_loc_df.sub2

ri_loc_df['mall_location'].str.lower()

ri_loc_df.columns = [col.lower() for col in ri_loc_df.columns]
            
