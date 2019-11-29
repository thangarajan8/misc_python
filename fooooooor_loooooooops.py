# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:59:36 2019

@author: Thanga
"""

import random
from timeit import timeit
from string import ascii_lowercase
from time import time

lower_list = [ascii_lowercase[:random.randint(0,25)] for i in range(1000000)]
upperlist = []
#1

def to_upper_1():
    upperlist = []
    for word in lower_list:
        upperlist.append(str.upper(word))
s_time = time()
to_upper_1()
print('Usual FOR LOOP {}'.format(time()-s_time))

#2
upper = str.upper
upperlist = []
append = upperlist.append

def to_upper_2():
    for word in lower_list:
        append(upper(word))
s_time = time()
to_upper_2()
print('Usual FOR LOOP exclude search {}'.format(time()-s_time))

#3
def to_upper_3():
    upperlist = []
    upper = str.upper
    append = upperlist.append
    for word in lower_list:
        append(upper(word))
    return upperlist
s_time = time()
upperlist = to_upper_3()
print('Usual FOR LOOP exclude search and global variables {}'.format(time()-s_time))

#4
upperlist = []
s_time = time()
upperlist = map(str.upper, lower_list)
print('Using MAP {}'.format(time()-s_time))

#5
s_time = time()
upperlist = [str.upper(x) for x in lower_list]
print('Using list comp {}'.format(time()-s_time))

#6
upperlist = []
s_time = time()
uppers = str.upper
upperlist = [uppers(x) for x in lower_list]
print('Using list comp exclude search {}'.format(time()-s_time))

timeit(to_upper_3,number =1000)

a_list = list(range(100000))
def checkIn():
    if 100000 in a_list:
        print(True)
timeit(checkIn, number=1000)

a_dict = {x:x for x in range(100000)}
def checkInDict():
    if not a_dict.get(100000,None):
        print(True)
timeit(checkInDict, number=1000)
