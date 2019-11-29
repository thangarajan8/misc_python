# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:21:24 2019

@author: Thanga
"""
def replace_str_index(text,index=0,replacement=''):
    text = '%s%s%s'%(text[:index],replacement,text[index+1:]) 
    return text

n = '11100'*100
k = 5
m = 2
str_list = []
re_count = 0
for i in range(0,len(n),k):
    word = n[i:i+k]
    one_count = word.count('1') 
    if one_count == m:
        str_list.append(word)
    else:
         if one_count > m:
             for i in range(one_count-m):
                 word = replace_str_index(word,word.find('1'),'0')
                 re_count += 1
         else:
             for i in range(m-one_count):
                 word = replace_str_index(word,word.find('0'),'1')
                 re_count += 1
         str_list.append(word)
            
print(re_count)
print(''.join(str_list))
