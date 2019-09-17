# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:41:01 2019

@author: 10541
"""

import fractions
def lcm(n): 
    ans = 1    
    for i in range(1, n + 1): 
#        print(fractions.gcd(ans, i))     
        ans = (ans * i)/fractions.gcd(ans, i)
        print(ans)
    return ans 
lcm(10)
