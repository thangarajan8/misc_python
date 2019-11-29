# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:55:32 2019

@author: Thanga
"""

def maxProfit(prices, n, k): 
      
    # Bottom-up DP approach 
    profit = [[0 for i in range(k + 1)] 
                 for j in range(n)] 
      
    # Profit is zero for the first 
    # day and for zero transactions 
    for i in range(1, n): 
          
        for j in range(1, k + 1): 
            max_so_far = 0
              
            for l in range(i): 
                max_so_far = max(max_so_far, prices[i] -
                            prices[l] + profit[l][j - 1]) 
                              
            profit[i][j] = max(profit[i - 1][j], max_so_far) 
      
    return profit 
  
   
x = [13,10,8,4,10]
print(x,len(x),len(x))
d = {}

for i in range(len(x)-1):
    profit = -(x[i]-x[i+1])
    d[i+1] = profit
        
print(max(d.values()))