# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:53:49 2019

@author: 10541
"""

def check_sum(li,num):
    flag = False
    for i in li:
        for j in li :
            if i+j==num:
                flag = True
                break
                
    return flag
def check_overlap(li):
    li_range = []
    for x in li:
        li_range += list(range(x[0],x[1]))
    if len(li_range) != len(set(li_range)):
        return True
    else:
        return False
print(check_sum(li=[11,1,2,3,10],num=21))


print(check_overlap(li=[[1,5], [8,9], [3,6]]))
print(check_overlap(li=[[1,5], [5,6]]))

