# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:56:45 2019

@author: 10541
"""

a = 'hello'
a[0]

a = [1,2,3]
id(a)
a[0] = 89

a = 'frame'
a[0]+a[-1]
a[0::len(a)-1]
a[0::-1]
a[-1:-len(a)-1:-1]
a[::-1]
'sathu beno'.replace(' ','')
names = ['sathish kumar','sohail pasha',
         'santosh ET','Sanjay Ranganathan',
         'Aparna Annadurai','Krithiga Aankar',
         'Govarthini Ponram','Beno Fernando',
         'Gopi Nath']
k = {}
for _ in names:
    ch = _[_.find(' ')+1]
    ord_c = ord(ch)
    k[ord_c] = ch
    
sorted(names,key=str.split(' ')[1][0])

def sname(name):
    def nsort(name_1):
        print(name_1)
        return name_1.split(' ')[1]
    
    return sorted(name,key=nsort)

sname(names)
import operator
sent = 'i will get my salary two day'
stats = [ {_:len(_)} for _ in sent.split(' ') if len(_)%2 == 0]

'beno' == 'beno'[::-1]
import random
a = 'abcdef'
b = 'ghij'
nums = list(range(0,len(a+b)))
nums_s = random.shuffle(nums)
import string
x = [ord(_) for _ in ['a','e','i','o','u']]
y = [ _ for _ in sent if ord(_) in x]
v = set(y)

c = 1
v = 5
print("Sum : {} {}".format(c+v,'dum'.lower()))
';'.join('thanga')

f"sum:{c+v}"


print('thanga',end='\b ')
import winsound
winsound.Beep(3000,50000)
