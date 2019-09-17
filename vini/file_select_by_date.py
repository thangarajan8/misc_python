# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 18:38:17 2018

@author: 10541
"""

from datetime import datetime
import os
now = datetime.now()
current_month = now.month
current_year = now.year
current_month_files = []
files = ['c:\\vini_20181224.csv','thanga_20181111.csv']


for file in files:
    file_created_date = str(os.path.basename(file).split('.')[0].split('_')[1])
    datetime_object = datetime.strptime(file_created_date,'%Y%m%d')
    if datetime_object.year == current_year and datetime_object.month == current_month:
        current_month_files.append(file)

data = [['1.pkl','99.08'],
        ['2.pkl','98.7']
        ]
import pandas as pd
df = pd.DataFrame(data,columns=['model_name','score'])
if not os.path.exists('sam.csv'):
    print('Createing new')
    df.to_csv('sam.csv',index=False,mode='a')
else:
    print('Appending')
    df.to_csv('sam.csv',index=False,mode='a',header=False)

file_path = 'E:\\learnings\\python\\vini\\folder\\'
files = os.listdir(file_path)
for file in files:
    file_name,file_ext = os.path.splitext(file)
    if file_ext != '.txt':
        delete_file = os.path.join(file_path,file)
        os.remove(delete_file)
        print(file)

import glob
image_paths = sorted(glob.glob(file_path+"key*.pkl"), key=os.path.getmtime)
