# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:00:02 2019

@author: Thangarajan
"""

import pandas as pd
import json

#list of list to pandas dataframe
data_list = [[1,2,3],[4,5,6],[6,7,8]]

list_df = pd.DataFrame(data_list,columns=['a','b','c'])

#pandas dataframe to list of dict => dataframe

data_dict = json.loads(list_df.to_json(orient='records'))
dict_df = pd.DataFrame(data_dict)

#dataframe to csv
dict_df.to_csv('dict_df.csv',index=False)

#dataframe to clipboard
dict_df.to_clipboard(index=False)


#column rename
list_df.rename(['a','b'],['x,y'])

#row wise total and column wise total
list_df['row_sum'] = list_df.iloc[:, 1:].sum(1)
list_df.loc['Total'] = list_df[['a','b','c','row_sum']].sum()
