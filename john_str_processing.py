# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 00:02:50 2018

@author: 10541
"""
from time import sleep
#ip1 = 'aaabbc'
ip1 = 'i am working in chennai and going to madurai now'

#sorted_ip1 = ''.join(sorted(ip2))

occ_dict = dict((letter,ip1.count(letter)) for letter in set(ip1))


key_min = occ_dict[min(occ_dict.keys(), key=(lambda k: occ_dict[k]))]
key_max = occ_dict[max(occ_dict.keys(), key=(lambda k: occ_dict[k]))]

iter_count = 0
while len(list(occ_dict)) > 0:
    iter_count += 1
    for key in list(occ_dict):
        print(key)
        value = occ_dict[key]
        if value == key_min:
            del occ_dict[key]
        else:
            occ_dict[key] = value - key_min
values = list(occ_dict.values())
occ_count_dict = dict((letter,values.count(letter)) for letter in set(values)) 
max_occ_count = occ_count_dict[min(occ_count_dict.keys(), key=(lambda k: occ_count_dict[k]))]

while len(list(occ_dict)) > 0:
    iter_count + 1
    values = list(occ_dict.values())
    occ_count_dict = dict((letter,values.count(letter)) for letter in set(values)) 
    max_occ_count = occ_count_dict[min(occ_count_dict.keys(), key=(lambda k: occ_count_dict[k]))]
    for key in list(occ_dict):
        value = occ_dict[key]
        occ_value = occ_count_dict[value]
        if value == occ_value:
            del occ_dict[key]
        