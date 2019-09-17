# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:15:47 2019

@author: Thangarajan
"""

import csv
import urllib.request

url = "http://winterolympicsmedals.com/medals.csv"
ftpstream = urllib.request.urlopen(url)
csvfile = csv.reader(ftpstream.read().decode('utf-8'))
for line in csvfile:
    print(line) 

