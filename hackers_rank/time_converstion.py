# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:57:59 2019
https://www.hackerrank.com/challenges/time-conversion/problem
@author: Thanga
"""


def convert_12_24(s):
    result = ''
    am = True
    if 'AM' in s:
        am = True
    else:
        am  = False    
    if not am:
        time_input_temp = s.replace('PM','')
        time_split = time_input_temp.split(':')
        hour = int(time_split[0])
        minute = int(time_split[1])
        second = int(time_split[2])
        if hour != 12:
            result = '{}:{}:{}'.format(hour+12,str(minute).zfill(2),str(second).zfill(2))
        else:
            result = '{}:{}:{}'.format(hour,str(minute).zfill(2),str(second).zfill(2))
    else:
        time_input_temp = s.replace('AM','')
        time_split = time_input_temp.split(':')
        hour = int(time_split[0])
        minute = int(time_split[1])
        second = int(time_split[2])
    
        if hour == 12:
            result = '{}:{}:{}'.format('00',str(minute).zfill(2),str(second).zfill(2))
        else:
            result = '{}:{}:{}'.format(str(hour).zfill(2),str(minute).zfill(2),str(second).zfill(2))
            
    return result
s = '12:45:54PM'

print(convert_12_24(s))