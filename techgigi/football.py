# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:45:05 2019

@author: Thangarajan
"""

for t in range(int(input())):
    dummy = int(input())
    goals = [i * 20 for i in list(map(int,input().split()))]
    fouls = [i * 10 for i in list(map(int,input().split()))]
    max_score = 0
    scores =[g-f if g-f > 0 else 0 for (g,f) in zip(goals,fouls) ]
        
            
        