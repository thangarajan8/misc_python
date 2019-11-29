# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:26:16 2019

@author: Thanga
"""

s = 'abcdcgh'

sub_s = []

for i in range(len(s)):
    sub_s.append(s[:i])
    
def lds(s):
    seens = {}
    start, end, curt_start = 0, 0, 0
    for curt_end, c in enumerate(s):
        try:
            last_seen = seens[c]
            if last_seen < curt_start:
                raise KeyError(f"{c!r} not found in {s[curt_start: curt_end]!r}")
            if end - start <  curt_end - curt_start:
                start, end = curt_start, curt_end
            curt_start = last_seen + 1
        except KeyError:
            pass
        seens[c] = curt_end
    else: 
        # case when the longest substring is suffix of the string, here curt_end
        # do not point to a repeating char hance included in the substring
        if s and end - start <  curt_end - curt_start + 1:
            start, end = curt_start, curt_end + 1
    return s[start: end]

print(lds(s))