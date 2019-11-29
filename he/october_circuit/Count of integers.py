# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:25:51 2019

@author: Thanga
"""
def calculate_factorial_multi_half(number):

        if number == 1 or number == 0:
            return 1

        handle_odd = False
        upto_number = number

        if number & 1 == 1:
            upto_number -= 1
            handle_odd = True

        next_sum = upto_number
        next_multi = upto_number
        factorial = 1

        while next_sum >= 2:
            factorial *= next_multi
            next_sum -= 2
            next_multi += next_sum

        if handle_odd:
            factorial *= number

        return factorial
def fact(n):
    if n==1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
from math import factorial
from itertools import permutations
testcases = int(input())
for testcase in testcases:
    dummy = input()
    counter = 0
    n=map(int,input().split())
    for i in n:
        fact = factorial(i-1)
        mod = fact % i
        if mod == i-1:
            counter += 1
    print(counter)
#    print('{} % {} = {} == {}'.format(fact,i,mod,i-1))
    
calculate_factorial_multi_half(10**8)
x = list(permutations(range(1,6)))
fact(5)
calculate_factorial_multi_half(11-1) % 11
