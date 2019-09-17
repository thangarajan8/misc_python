# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:25:29 2019

@author: 10541
"""

y = [-1, 7, 8, -5, 4] 
#y = [3, 2, 1, -1] 
y = [11,12,-2,-1]
y = [4,5,4,3]
y = [5, 10, 4, -1]
t = []
max_sum = 0
max_sum_list = []
for i in range(len(y)):
    for j in range(len(y)):
        i_index = i
        j_index = j
        if i_index != j_index and abs(i_index-j_index) != 1 and j_index-i_index > 0:
            ij = [y[i],y[j]]
            t.append(ij)
            if sum(ij) > max_sum:
                max_sum = sum(ij)
    
for k in t:
    if sum(k) == max_sum:
        max_sum_list.append(k)

if len(max_sum_list) == 1:
    res = max_sum_list[0]
    if res[0] > 0 and res[1] > 0:
        res = [ str(_) for _ in max_sum_list[0]]
        print(''.join(reversed(res)))
    else:
        print(str(max(res)))
else:
    maxi = 0
    index = 0
    for m in range(len(max_sum_list)):
        if maxi < max_sum_list[m][0]:
            maxi = max_sum_list[m][0]
            index = m
    res = max_sum_list[index]
    if res[0] > 0 and res[1] > 0:
        res = [ str(_) for _ in max_sum_list[0]]
        print(''.join(res))
    else:
        print(str(max(res)))
#    ans = [str(_) for _ in reversed(ans)]
#    print(''.join(ans))
#     
import itertools
t = y
c = list(itertools.combinations(t, 2))
c
set(c)
