#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'sortedSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from operator import mul
def sortedSum(a):
    # Write your code here
    total = 0
    print(len(a))
    m = (pow(10,9)+7)
    for i,j in enumerate(a):
        lst = sorted(a[:i+1])
        r_list = range(1,i+2)
        total += sum(list(map(mul,lst,r_list)))
        # for x,y in zip(lst,r_list):
            # total += x*y
    print(total)
    return total % m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(raw_input().strip())

    a = []

    for _ in xrange(a_count):
        a_item = int(raw_input().strip())
        a.append(a_item)

    result = sortedSum(a)

    fptr.write(str(result) + '\n')

    fptr.close()
