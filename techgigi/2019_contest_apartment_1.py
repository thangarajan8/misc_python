# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:27:57 2019

@author: 10541
"""

#y = [-1, 7, 8, -5, 4] 
#y = [3, 2, 1, -1] 
#y = [11,12,-2,-1]
#y = [4,5,4,3]
#y = [5, 10, 4, -1]
y = [-2,-3,-4,-5]
t = []
res = []
max_sum = None
max_ne = []
for i in range(len(y)):
    for j in range(len(y)):
        i_index = i
        j_index = j
        if i_index != j_index and abs(i_index-j_index) != 1 and j_index-i_index > 0:
            ij = [y[i],y[j]]
            t.append(ij)
            if max_sum is None:
                max_sum = sum(ij)
                max_ne = ij
            elif max_sum <= sum(ij):
                max_sum = sum(ij)
                max_ne.append(ij)
x = ['bba','abb','abb']
count = 0
[1 for i, j in zip(a, a) if i == j[:: -1]]
zip(a,a)
for i,j in zip(a,a):
    print(i,j[::-1])
    if i == j[::-1]:
        count += 1
        
import itertools
for a, b in itertools.combinations(x, 2):
    if a == b[::-1]:
        count+= 1
        
print('rasanlu')