# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:04:36 2020

@author: Thanga
"""

import pandas as pd

df = pd.read_csv('TA_Ageing_Details_from2014.csv')

#df['TA_DISB_DATE'] =  pd.to_datetime(df.TA_DISB_DATE, format='%d/%m/%Y')
#df['LOS_DISB_DATE'] = pd.to_datetime(df.LOS_DISB_DATE.split(' ')[0], format='%d/%m/%Y')
#df['LOS_DISB_DATE'] = df.apply(lambda x : pd.to_datetime(x['LOS_DISB_DATE'].split(' ')[0], format='%d/%m/%y'),axis=1)

dcode = '1001'
agmtno = 'TN3000TA03649'
df['SZDEALERCODE'] = df['SZDEALERCODE'].astype(str)
df_1001 = df[(df['SZDEALERCODE']==dcode)]


df_1001['TA_DISB_DATE'] =  pd.to_datetime(df_1001.TA_DISB_DATE, format='%d/%m/%Y')
df_1001['LOS_DISB_DATE'] = pd.to_datetime(df.LOS_DISB_DATE, format='%d/%m/%Y %H:%M')
#df_1001['LOS_DISB_DATE'] = df_1001.apply(lambda x : pd.to_datetime(x['LOS_DISB_DATE'].split(' ')[0], format='%d/%m/%y'),axis=1)
