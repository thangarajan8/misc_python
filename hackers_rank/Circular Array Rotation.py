# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:42:06 2019
https://www.hackerrank.com/challenges/circular-array-rotation/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
@author: Thanga
"""

a = [1,2,3]
b = [1,2,3]
rotate_count = 10
for i in range(rotate_count%len(a)):
    a.insert(0,a.pop())
    print(a,b)



