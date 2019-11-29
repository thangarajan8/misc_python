# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:27:29 2019
https://www.hackerearth.com/problem/golf/sleep-sleep-repeat/
@author: Thanga
"""

from datetime import date, timedelta
dstart = date(2019,10,1)
dend = date(2021,10,31)
days = [dstart + timedelta(days=x) for x in range((dend-dstart).days + 1) if (dstart + timedelta(days=x)).weekday() not in [5,6]]

for d in days:
    print("{date.day}.{date.month}.{date.year}".format(date=d))
    
    
#import pandas as pd
#df = pd.DataFrame({'date':days})
#df.to_csv('work.csv',index=False)



