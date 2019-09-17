# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:04:57 2019

@author: Thangarajan
"""


def generate_ngrams(s):
    ngrams = []
    token = list(s)
    for i in range(1,len(s)):
        ngram = zip(*[token[i:] for i in range(i)])    
        ngrams += ngram
    return ["".join(ngram) for ngram in ngrams]
text = 'thanga'
X = generate_ngrams(text)


def pref(string): 
    prefs = []
    start, end = 0, 0
       
    while start < len(string):          
        if string[end] == string[end-start]:              
            prefs.append(string[start:end + 1] )
            end += 1             
            if end == len(string): 
                start += 1
                end = start          
        else: 
            start += 1
            end = start 
    return prefs

def suf(string): 
       
    start, end = -1, -1
       
    while start < len(string):          
        if string[end] == string[end-start]:              
            print(string[start:end + 1], end= " ") 
            end += 1             
            if end == len(string): 
                start += 1
                end = start          
        else: 
            start += 1
            end = start         
Y = pref(text)
suf(text)
s ='nothing'
suffixes = [s[i:] for i in range(1,len(s))]
D = [s[i:] for i in range(-len(s)+1,0)]
