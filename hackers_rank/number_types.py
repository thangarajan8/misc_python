# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:42:05 2019

@author: 10541
"""
number = 99
rjust_count = len(bin(number)[2:])
for i in range(1,number+1):
    print ("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(i,len("{0:b}".format(number))))