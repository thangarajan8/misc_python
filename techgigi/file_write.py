# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 15:47:09 2019

@author: Thangarajan
"""
from ast import literal_eval
def reads(name):
    count = 0
    with open('naveen.txt') as f:
#        x = f.readlines()
        for y in f:
            d = literal_eval(y)
            if d['name'] == name:
                count += 1
    return count,name
        
import random
import time
lts = ['sanjay','aparna','naveen','sohail','beno','deepa','govarthini','santosh',
       'davanya','thanga','sathish',]
#with open('naveen.txt','w') as f:
#    for i in range(1000000):
#        f.write("{'name':'%s'} \n"%lts[random.randint(0,len(lts)-1)])
        
start_time = time.time()
count,name = reads('thanga')
end_time = time.time()
print('Total time {}'.format(end_time-start_time))