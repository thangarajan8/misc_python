# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:26:27 2019

@author: Thangarajan
"""

def prefix(string): 
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

def calculateScore(text, prefixString, suffixString):
    total_score = len(prefixString)+len(suffixString)
    prefs = prefix(text)
    sufs  = [text[i:] for i in range(1,len(text))]
    pref_max = 0
    pref = None
    suf = None
    pref_match = []
    suf_match = []
    for p in prefs:
#        print(p)
        if p in prefixString :
            pref_match.append(p)
            if pref_max < len(p):
                pref_max = len(p)
                pref  = p
    suf_max = 0
    for s in sufs:
        suf_match.append(s)
        if s in suffixString:
            if suf_max < len(s):
                suf_max = len(s)
                suf = s
    print(pref_max,suf_max)
    print(pref,suf)
    print(pref_match,suf_match)
    if pref_max == suf_max:
        print(pref,suf)
        return min([prefixString,suffixString])
    else:
        return text
a = 'abracadabra'
b = 'habrahabr'
c = 'bracket'
s = calculateScore(a,b,c)
pref = prefix(a)
text = a
sufs  = [text[i:] for i in range(1,len(text))]
