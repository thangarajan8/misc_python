# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 17:00:47 2019
https://www.hackerrank.com/challenges/minimum-distances/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
@author: Thanga
"""

def minimumDistances(a):
    dist = len(a)
    for i in range(len(a)):
        for j in range(i,len(a)):
            if i != j:
                if a[i] == a[j]:
                    if dist > abs(i-j):
                        dist = abs(i-j)
#                    dist.append(abs(i-j))
                else:
                    dist = -1
    return dist
s = '1 2 3 4 10'*10000
a = list(map(int,s.split(' ')))

print(minimumDistances(a))