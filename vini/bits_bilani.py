# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:03:58 2019

@author: Thanga
"""
import pandas as pd
def file_to_line_list(file_path):
    return pd.read_csv(file_path,delimiter='\t')
    
sms_df = file_to_line_list('sms_dataset_1573053388397.dat')

