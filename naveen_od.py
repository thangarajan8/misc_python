# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:43:54 2018

@author: 10541
"""
import sys
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")
import os,glob
import pandas as pd
from logzero import logger
file_path = 'C:\\Users\\10541\\Desktop\\filesplit\\'
file_list = image_paths = sorted(glob.glob(file_path+"*.csv"), key=os.path.getmtime)
forecast_out2 = pd.DataFrame()
op_df_l = []
class_list = ['Business','PremiumEconomy','Economy']
count = 1
#df_a = pd.read_csv('C:\\Users\\10541\\Desktop\\filesplit\\CGP-DAC_RX0716_CCU.csv')
for j in file_list[:5]:
    logger.info('Processing {}----{}'.format(j,count))
    count += 1
    
    for c in class_list:
        df_b = pd.read_csv(j)
        try:
            
            logger.info('Processing for {}'.format(c))
            
            df_a = df_b[df_b['BookingClass'] == c]
            df_a['FlownYear'] = df_a['FlownYear'].astype(str)
            df_a['FlownMonth'] = df_a['FlownMonth'].astype(str)
            df_a['FlownMonth'] = [b.zfill(2) for b in df_a['FlownMonth']]
            df_a['year_month'] = df_a['FlownYear'] + df_a['FlownMonth']
            #this subsetting is temporary
            df_a = df_a[df_a['FlownYear'] != '2019']
            #df_a = df_a[(df_a['year_month'] != '201806') & (df_a['year_month'] != '201807') & (df_a['year_month'] != '201808') & (df_a['year_month'] != '201809') & (df_a['year_month'] != '201810') & (df_a['year_month'] != '201811') & (df_a['year_month'] != '201812')]
            df_a['FlownYear'] = df_a['FlownYear'].astype(int)
            df_a.sort_values('FlownYear',axis=0,inplace=True)
            df_a.reset_index(drop=True,inplace=True)
#            print(df_a)
#            print(list(df_a['FlownYear'])[-1])
            n = int(df_a['FlownYear'][-1:].values)
            #df_a = df_a.groupby(['BookingYear','BookingWeek',''])
            df_r = df_a.copy()
            df_r['FlownYear'] = df_r['FlownYear'].astype(str)
            df_r['FlownWeek'] = df_r['FlownWeek'].astype(str)
            df_r['FlownWeek'] = [a.zfill(2) for a in df_r['FlownWeek']]
            df_r['year_week'] = df_r['FlownYear'] + df_r['FlownWeek']
            df_r.sort_values('year_week',axis=0,inplace=True)
            df_r.reset_index(drop=True,inplace=True)
            d = int(df_r['FlownWeek'][-1:].values)
            df_a['FlownWeek'] = df_a['FlownWeek'].astype(int)
            for i in range(23,23+24):
                #For 2018 Flown and bookings
                df_a1 = df_a[df_a['FlownYear']== n]#we will get all the 2018 data
                df_a1 = df_a1[df_a1['FlownWeek']==i]#we will get that week from flown 2018
                df_a1 = df_a1[df_a1['BookingYear'] == n]#we get booking year as n from flown 2018 fro that week
                df_a1 = df_a1[df_a1['BookingWeek'] < i]
                
                
                #For 2017 flown and booking
                df_a2 = df_a[df_a['FlownYear']== n-1]
                df_a2 = df_a2[df_a2['FlownWeek']==i]
                df_a2 = df_a2[df_a2['BookingYear'] == n-1]
                df_a2 = df_a2[df_a2['BookingWeek'] < i]
                
                #df_y = df_a[df_a['FlownYear']==n-1]
                #df_y = df_y[df_y['FlownWeek']==i]
                #df_y = df_y[df_y['BookingYear'] == n-1]
                #df_y = df_y[df_y['BookingWeek'] < i]
                
                df_a1_b = df_a1.groupby(['BookingYear','FlownYear','POS','Route','BookingClass'],as_index=False).agg({'Revenue':'sum','Passengercount':'sum'})
                #df_a1_b = df_a1_b[df_a1_b['BookingYear'] != n-1]
                df_a1_b['AvgFare'] = df_a1_b['Revenue']/df_a1_b['Passengercount']
                
                df_a2_b = df_a2.groupby(['BookingYear','FlownYear','POS','Route','BookingClass'],as_index=False).agg({'Revenue':'sum','Passengercount':'sum'})
                #df_a2_b = df_a2_b[df_a2_b['BookingYear'] != n-1]
                df_a2_b['AvgFare'] = df_a2_b['Revenue']/df_a2_b['Passengercount']
                
                #df_y_b = df_y.groupby(['BookingYear','FlownYear','POS','Route','BookingClass'],as_index=False).agg({'Revenue':'sum','Passengercount':'sum'})
                #df_y_b =  df_y_b[df_y_b['BookingYear'] != n-1] 
                #df_y_b['AvgFare'] = df_y_b['Revenue']/df_y_b['Passengercount']
                
                df_a1_b['Avg_faren'] = df_a1_b['AvgFare'].copy()
                #print(df_y_b)
                #df_a1_b['yieldn'] = df_a1_b['Avg_faren'].copy()
                #df_a1_b.loc[df_a1_b['BookingYear'] == n, 'Avg_faren'] = df_a1_b['AvgFare'].copy()
                
                #df_a2_b['Avg_faren-1'] = df_a2_b['AvgFare'].copy()
                #df_a2_b.loc[df_a2_b['BookingYear'] == n-1, 'Avg_faren-1'] = df_a2_b['AvgFare'].copy()
                
                #k = len(df_y[df_y['FlownYear']==n-1])
                #df_y_b['yieldn-1'] = df_y_b['AvgFare'].copy()
                
                df_data = df_a1_b[['FlownYear','Avg_faren']]
                df_data['Avg_faren-1'] = df_a2_b['AvgFare'].copy()
                df_data['var_yld'] = ((df_data['Avg_faren']-df_data['Avg_faren-1'])/df_data['Avg_faren-1'])+1
                df_data['yieldn-1'] = df_a2_b['AvgFare'].copy()
                df_data['yieldn'] = df_a1_b['AvgFare'].copy()
                if len(df_data['var_yld'])>0:
                    if (df_data['var_yld'][0]>1.6):
                        df_data['yield_FCT'] = 1.6*df_data['yieldn']
                    else:
                        df_data['yield_FCT'] = df_data['var_yld']*df_data['yieldn']

                df_data['FlownWeek'] = i
                df_data['Class'] = c
                
                #if(df_data['FlightNo'].isnull().any()):
                #    df_data['FlightNo'] = j.split('_')[1]
                if(df_data['FlownYear'].isnull().any()):
                    #df_data['yield_FCT'] = df_data['yieldn-1']
                    df_data['FlownYear'] = n
                if(df_data['Avg_faren'].isnull().any()):
                    df_data['yield_FCT'] = df_data['yieldn-1'].copy()
                if(df_data['Avg_faren-1'].isnull().any()):
                    df_data['yield_FCT'] = df_data['yieldn'].copy()
                file_name = os.path.basename(j)
                df_data['Route'] = file_name.split('_')[0]
                #df_data['FlightNo'] = j.split('_')[1]
                df_data['FlightNo'] = file_name.split('_')[1]
                df_data['POS'] = file_name.split('_')[2].split('.')[0]
                op_df_l.append(df_data)
#                forecast_out2 = pd.concat((forecast_out2,df_data),axis=0)
                
        except TypeError:
#            raise
            print(j + 'TypeError')
            pass
logger.info(len(op_df_l))
df = pd.concat(op_df_l)
df.to_csv('thanga.csv')