# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:19:43 2019
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
@author: Thanga
"""

def reverse_number(n):
    rev = 0
    while n != 0:
        remainder = n % 10
        rev = (rev*10) + remainder
        n = int(n / 10)
    return rev

i,j,k = 4367,83740901,4367
counter = 0
for m in range(i,j+1):
    rev_number = reverse_number(m)
#    rev_number = int(str(m)[::-1])
    if abs(m-rev_number)%k == 0:
        counter += 1
        
        
        
reverse_number(87686869896)
