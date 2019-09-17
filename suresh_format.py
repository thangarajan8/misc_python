# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:02:33 2018

@author: 10541
"""
import copy
bill_id = '1234'
bill_split = []
temp = ''
char = '*'
num = '#'
hchar = '$'
schar = '@'
k = ''
for i in bill_id:
    acode = ord(i)
    if (acode >= 65 and acode <= 90) or (acode >= 97 and acode <= 122):
       print('char')
       temp = temp+char
    elif acode == 45:
        temp = temp + hchar
        print('hypen')
    elif acode == 47:
        temp = temp+schar
        print('slash')
    else:
        temp = temp+num
        print('number')
#j = len(temp)-1 
#c = temp
#print(c)
##["".join(g) for k, g in groupby(c) if k != '#']
#ans = ''
#for index in range(len(temp)-1):
#    if temp[index] == temp[index+1] :
#        ans = ans+temp[index]
#    elif  temp[index] == temp[index-1]:
#        ans = ans+temp[index]+'|'
#    else:
#        ans = ans+ temp[index]+'|'
#
#print(ans)
#result = []
#slen = 0
#start = 0
#ansl = ans.split('|')
#end = len(ansl[0])
#try:
#    for k in range(len(ansl)):
#        print(ansl[k])
#        word = bill_id[start:end]
#        print(start,end)
#    #    end = len(ansl[k])
#        start = start + len(ansl[k])
#        end = end + len(ansl[k+1])
#        result.append(word)
#except Exception:
#    result.append(ansl[k])
#    pass
##    break
#print(result)