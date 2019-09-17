# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:14:07 2019

@author: 10541
"""

def get_median(numbers):
    print(len(numbers))
    if len(numbers) % 2 == 0:
        print('i am here')
        return numbers[int(len(numbers)/2)+1]
    else:
        sorted_numbers = sorted(numbers)
        m1 = sorted_numbers[int(len(sorted_numbers)/2)]
        m2 = sorted_numbers[int(len(sorted_numbers)/2)-1]
        median = (m1+m2)/2
        return int(median)
import sys
lines = sys.stdin.readlines()
# print(lines)
numbers = [3, 7, 8, 5, 12, 14, 21, 13, 18]

x = get_median(numbers)
print(x)
if len(numbers) % 2 == 1:
    numbers.remove(x)
lower_half = [i for i in numbers if i < x]
upper_half = [i for i in numbers if i > x]
l = get_median(lower_half)
u = get_median(upper_half)
print(lower_half)
print(upper_half)
# print(l)
# print(x)
# print(u)