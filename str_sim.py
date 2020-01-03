# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:02:05 2019
https://www.hackerrank.com/challenges/string-similarity/problem
@author: Thanga
"""

a = 'ababaa'

    
iters = 0    
def stringSimilarity(s):
    global iters
    counter = 0
    for j in range(len(s)):
        word = s[j:]
        if word[0] == s[0]:
            for m,n in zip(s,word):
                iters += 1
                if m == n:
                    counter += 1
                else:
                    break
    print(iters)
    return counter

print(stringSimilarity(a))
