# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 18:02:30 2019

@author: Thangarajan
"""

def bin_mad(n):
    bin_n = bin(n)[2:]
    count = 0
    for k in range(len(bin_n)):
        word = bin_n[k:]
        rows = len(word)
        for i in range (0,rows):
            l = ''
            for j in range(0, i + 1):
#                print(j, end=' ')
                l += word[j]
            if l.count('0') % 2 != 0:
                count += 1
    return count

0
1
2
10
17
32
33
127
341
455
496
992
1000
430510914326
8470634074737128636070224
9893020956
3846435266552999150
977354604222
27055031064
6702565932198233123811
427738644490
65146
89623387
3773561366613203692478122629384
bin_mad(256651750668965698947092)
