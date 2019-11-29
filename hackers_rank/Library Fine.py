# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:01:31 2019

https://www.hackerrank.com/challenges/library-fine/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

@author: Thanga
"""

def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    if d1 == d2:
        if m1 == m2:
            if y1 == y2:
                fine = 0
            else:
                fine = 10000
        else:
            fine = abs(m2-m1) * 500
    elif m1 == m2:
        fine = 0
    else:
        fine = abs(d2 - d1) * 15
        
    return fine
    
    

    
fine = libraryFine(9,6,2015,6,6,2015)
print(fine)
a = [1,2,3]
isinstance(a,list)
