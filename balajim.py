# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:40:53 2018

@author: 10541
"""

import pandas as pd
from collections import Counter

df = pd.read_csv('tenant.csv')

sale_list = list(df['NET_SALES'])
sale_count = Counter(sale_list)

sales_count = [[x,sale_list.count(x)] for x in set(sale_list)]

for i in range(2,40,6):
    print(i)