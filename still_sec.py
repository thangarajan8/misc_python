# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:28:49 2019

@author: Thanga
"""


from datetime import datetime
#while True:
s_date = datetime.strptime('25-09-2019 09:00:00', '%d-%m-%Y %H:%M:%S')
n_date = datetime.now()
e_date = datetime.strptime('30-09-2020 18:30:00', '%d-%m-%Y %H:%M:%S')
total_second = (e_date-s_date).total_seconds()
remain_second = (e_date-n_date).total_seconds()
Percentage = ((int(total_second-remain_second))/int(total_second))*100
Percentage_remaining = (remain_second/total_second) * 100
print('Total Seconds =>     {}'.format(int(total_second)))
print('Passed Seconds =>    {}'.format(int(total_second-remain_second)))
print('Percentage Completed => {} %'.format(Percentage))
print('Percentage Remaining => {} %'.format(Percentage_remaining))