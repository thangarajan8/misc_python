# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:02:57 2019
https://www.hackerrank.com/challenges/ashton-and-string/problem
@author: Thanga
"""

s = """dbac"""*1000
k = 3
test_word = 'aacbbabaccddbdbadbac'*10
s_list = {}
s_set = set()
iters = 0
for i in range(len(s)):
   for j in range(i+1,len(s)+1):
       iters += 1
       s_list[s[i:j]] = None
       s_set.add(s[i:j])
       
word = sorted(s_list.keys())

result = word[k]
