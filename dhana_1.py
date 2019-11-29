# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:33:28 2019

@author: Thanga
"""

a="abcdcgh"
strLength = len(a)
dct={}
resStrLen=0
cnt=0
l=0
r=0
strb=l
stre=l
while(l<strLength and r<strLength):
    if a[l] in dct:
        if cnt>resStrLen:
            resStrLen=cnt
            strb=r
            stre=l
        dct.pop(a[r])
        cnt=cnt-1
        r+=1    
    else:
        cnt+=1
        dct[a[l]]=1
        l+=1

if cnt>resStrLen:
    resStrLen=cnt
    strb=r
    stre=l

print ("Result String : " + a[strb:stre])

