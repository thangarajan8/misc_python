# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:14:02 2019

@author: Thanga
"""
from random import randint
from time import sleep

executed_times = 0
try:
    while True:
        print("{} iteration started".format(executed_times + 1))
        sleep(randint(1, 5))
        executed_times += 1
        print("I am executing {} iteration".format(executed_times))
except KeyboardInterrupt:
    print("{} times the loop exexcuted".format(executed_times))
