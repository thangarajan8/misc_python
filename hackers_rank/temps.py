# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:52:15 2019

@author: 10541
"""


from collections import Counter


s = input().strip()
c = Counter(s).most_common()
print(type(c))
for element in sorted(c, key=lambda x: (-x[1], x[0]))[:3]:
    print(" ".join(str(e) for e in element), sep=" ")
