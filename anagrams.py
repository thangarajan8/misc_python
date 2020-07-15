#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    # Write your code here
    d = [ ''.join(sorted(i)) for i in dictionary]
    d1 = {}
    for k in d:
        if k in d1.keys():
            d1[k] = d1[k]+1
        else:
            d1[k] = 1
    occ = []
    d_list = list(d1.keys())
    print(d)
    if d:
        for q in query:
            s = ''.join(sorted(q))
            if s in d_list:
                occ.append(d1[s])
            else:
                occ.append(0)
    return occ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(raw_input().strip())

    dictionary = []

    for _ in xrange(dictionary_count):
        dictionary_item = raw_input()
        dictionary.append(dictionary_item)

    query_count = int(raw_input().strip())

    query = []

    for _ in xrange(query_count):
        query_item = raw_input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
