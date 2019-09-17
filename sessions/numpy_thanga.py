# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:01:09 2019

@author: Thangarajan
"""

import numpy as np
from scipy.stats import mode

#1
one_dim = np.array(range(0,500))
two_dim = one_dim.reshape(500,1)
three_dim = one_dim.reshape(10,10,5)

mul = np.multiply(one_dim,two_dim)
iden_int = np.identity(3,dtype=np.int32)
iden_float = np.identity(3,dtype=np.float32)

iden_int_X_iden_float = np.multiply(iden_int,iden_float)

np_arange = np.arange(1,100,2,dtype=np.int64)
np_arange_list = np_arange.tolist()

np.min(one_dim)
np.max(one_dim)

A = np.arange(1,10).reshape(3,3) 
B = np.arange(0,3)
vals = []
for i in B:
    vals.append(A[i,i])    
    

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b]) 

a[np.arange(4), b] += 10
a.shape
a.dtype

a_t = a.transpose()

tf = A > 2 
np.mean(A)
np.average(A)
np.bincount(A)
mode(A,axis=0)

