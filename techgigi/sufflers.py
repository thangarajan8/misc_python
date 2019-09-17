# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:21:01 2019

@author: Thangarajan
"""

A = 130

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
A = str(A)

if len(A) % 2 == 0:
    s = ''
    half = int(len(A)/2)
    for i in range(half):
        print(A[i],A[-(i+1)])
        s += A[i]+A[-(i+1)]
else:
    s = ''
    mid = int(len(A)/2)
    A = remove_char(A,mid)
    for i in range(mid):
        print(A[i],A[-(i+1)])
        s += A[i]+A[-(i+1)]
    s +='3'
    