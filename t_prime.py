# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:57:28 2019

@author: Thanga
"""
import math

def isPrime(n):

    # Corner cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def printDivisors(n):

    # Note that this loop runs till square root
    nums = []
    i = 1
    while i <= math.sqrt(n):

        if n % i == 0:

            # If divisors are equal, print only one
            if n / i == i:
                if isPrime(i):
                    nums.append(i)
            else:
                # Otherwise print both
                print(i, n / i)
                if isPrime(i):
                    nums.append(i)
                if isPrime(n/i):
                    nums.append(n/i)
        i = i + 1
    return nums
X = printDivisors(4)
X.append(1)


