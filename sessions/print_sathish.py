# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:09:56 2019

@author: Thangarajan
"""

#1
print('hello world')

#2
a = 12.12345

print('%.2f'%a)

#3
name = 'thanga'

print('Welcome {}'.format(name.capitalize()))


#4 print double quote

print('"')


#5

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('thanga',file=open('sample.txt','w'))
