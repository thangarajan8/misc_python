# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:25:09 2019
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
@author: Thanga
"""

#first iter
n,k,ar= (6,3,[1,3,2,6,1,2])
counter = 0
iters = 0
for i in range(n):
    for j in range(n):
        iters += 1
        if i != j :
            if (ar[i]+ar[j]) % k == 0:
                counter += 1
print('Answer : {}'.format(counter/2))
print(iters)


counter = 0
iters = 0
for i in range(n):
    for j in range(i,n):
        iters += 1
        if i != j :
            if (ar[i]+ar[j]) % k == 0:
                counter += 1
print('Answer : {}'.format(counter))
print(iters)


def divisibleSumPairs(n, k, ar):
    nums = [0] * k
    count = 0
    for ele in ar:
        modu = ele % k
        count += nums[(k - modu) % k]
        nums[modu] += 1
    return count

print(divisibleSumPairs(n,k,ar))
