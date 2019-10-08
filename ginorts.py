# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:48:10 2019

@author: Thanga
"""
def even(x):
    if int(x) % 2 == 0:
        return x
def odd(x):
    if int(x) % 2 != 0:
        return x
def sorter(word,function):
    filtered = list(filter(function,word))
    filtered_word = functools.reduce(lambda a,b:a+b, filtered)
    word_dict = dict.fromkeys(filtered_word)
    word_dict_orderd = eval(pprint.pformat(word_dict))
    sorted_letters = list(word_dict_orderd.keys())
    return functools.reduce(lambda a,b : a+b, sorted_letters)  

def num_sorter(numbers,function):
    even_nums = list(filter(function,numbers))      
    return functools.reduce(lambda a,b : a+b , even_nums)
import functools
import pprint
word = "Sorting1234"
expected_result = "ginortS1324"
#d = dict(zip(word,list(map(ord,word))))
#
#
#
#result_tuples = sorted(d.items(), key=lambda kv: kv[0], reverse=True)
#result = [i[0] for i in result_tuples]
#lower = list(filter(str.islower,word))
#upper = list(filter(str.isupper,word))
#numbers = list(filter(str.isdigit,word))
#even_num = list(filter(even,numbers))
#odd_num = list(filter(odd,numbers))
#
#lower_word = functools.reduce(lambda a,b: a+b,lower)
#
#l_dict = dict.fromkeys(lower_word)
#y = pprint.pprint(l_dict)
#y = pprint.pformat(l_dict)

l = sorter(word,str.islower)
u = sorter(word,str.isupper)
numbers = list(filter(str.isdigit,word))
even_num = num_sorter(numbers,even)
odd_num = num_sorter(numbers,odd)
result = '{}{}{}{}'.format(l,u,odd_num,even_num)
print(result)

print(*sorted(word, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
print(*sorted(word, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)))
