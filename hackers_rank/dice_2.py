# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:42:43 2019

@author: 10541
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 18:38:46 2019

@author: 10541
"""

number_dice = 2
x = 0
y = 0
probs = []
for i in range(1,7):
    for j in range(1,7):
        y += 1
#        probs.append(i+j)
        if i+j == 6 and (i!=j):
            probs.append([i,j])
            x += 1
        
            
