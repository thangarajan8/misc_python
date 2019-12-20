def parse_date(value):
    return datetime.strptime(value,'%d/%m/%Y').date()

import pandas as pd
from datetime import datetime
import json
now = datetime.now().date()

user_df = pd.read_csv('data.csv')
new_cols = {'identifier':'id','addressline':'line','adressType':'type','qualification':'qualification'}
user_df.rename(columns=new_cols, inplace=True)
user_df['dob'] = user_df['dob'].apply(parse_date)
user_df['age'] = (now - user_df['dob']).astype(str)
distinct_user_id = user_df['id'].unique()

d_list = []

for user in distinct_user_id:
    d = {}
    per_df = user_df[(user_df['id']== user)][['id','name','dob','qualification','age']]
    for col in per_df:
        if len (per_df[col].unique()) == 1:
            d[col] = per_df[col].unique()[0]
        else:
            d[col] = per_df[col].unique().tolist()
    addr_df = user_df[(user_df['id']== user)][['type','line', 'city', 'state']]
    dedup = addr_df.drop_duplicates(keep='first')
    address = dedup.to_dict(orient='records')
    d['addresses'] = address
    d_list.append(d)
    
result = {"users":d_list}
