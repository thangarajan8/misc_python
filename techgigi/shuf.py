# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:49:49 2019

@author: Thangarajan
"""

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
def solution(A):
    # write your code in Python 3.6
    A = str(A)

    if len(A) % 2 == 0:
        s = ''
        half = int(len(A)/2)
        for i in range(half):
            s += A[i]+A[-(i+1)]
    else:
        s = ''
        mid = int(len(A)/2)
        B = remove_char(A,mid)
        for i in range(mid):
            s += B[i]+B[-(i+1)]
        s +=A[mid]
    return int(s)
A = 1802
print(solution(A))