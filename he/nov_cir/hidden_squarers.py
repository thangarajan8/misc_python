# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:15:02 2019

@author: Thanga
"""

import math
# Example points in 3-dimensional space...
x = (1,1)
y = (2,20)
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Euclidean distance from x to y: ",distance)