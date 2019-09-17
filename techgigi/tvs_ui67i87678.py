# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:01:21 2019

@author: Thangarajan
"""

def createMatrix(rowCount, colCount, dataList):
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)

    return mat

lis = list(range(100 
v = createMatrix(3,3,lis)

c = [input1[i:i+3] for i in range(0,9,3)]
