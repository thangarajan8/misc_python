# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:12:22 2019

@author: Thanga
"""
import pandas as pd
import json
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    if (n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n%5 == 0 or n%7 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
x = []
for i in range((10**8)+1):
    if isPrime(i):
        x.append(i)
        print(i)
df =pd.DataFrame({'value':x})
df.to_csv('prime.csv', index = False)
df = pd.read_csv('prime.csv')
x = dict.fromkeys(df['value'].tolist())
with open('sam.txt','w') as f:
    f.write(json.dumps(x))