# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:13:28 2019

@author: Thanga
"""

def commonprefix(strings):
    s1 = min(strings)
    s2 = max(strings)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return ''

strings = ["abcdef", "abcghi", "abcabc"]
x = ["abcdef","adegh","a"]
print(commonprefix(x))

lis = [all(strings[i] == strings[i+1] for i in range(len(x)-1)) for x in zip(*strings)]

print (x[0][:lis.index(0) if lis.count(0) > 0 else len(lis)])


b = zip(*x)
c = [x[0] for x in b if x==(x[0],)*len(x)]
result = "".join(c)
