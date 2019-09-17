# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:19:13 2019

@author: 10541
"""

import pandas as pd
from ast import literal_eval

df = pd.read_csv('credits.csv')

    
X  = df['cast'].tolist()[0]
df['cast'] = df['cast'].apply(literal_eval)
df['crew'] = df['crew'].apply(literal_eval)
casts = []
crews = []
for index,row in df.iterrows():
    credits_id = row['id']
    
    for cast in row['cast']:
        cast['id'] = credits_id
        casts.append(cast)
    
    for crew in row['crew']:
            crew['id'] = credits_id
            crews.append(crew)
        
        
casts = pd.DataFrame(casts)
crew = pd.DataFrame(crews)
casts.to_csv('casts.csv',index=False)
crew.to_csv('crews.csv',index=False)
