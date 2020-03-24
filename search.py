# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:40:44 2020

@author: Thanga
"""

class Search():
    
    def __init__(self,data,search_item):
        self.data= data
        self.search_item = search_item
        pass
    
    def linear(self,search_item=None):
        """
        if element is found you will get a postive integer which is the index of
        the search element else -1 
        """
        for index,element in enumerate(self.data):
            if element == search_item:
                return index
                break
        return -1
             
    def binary(self):
        len_data = len(data) - 1
        left = 0
data = [1,2,3]    
s = Search([1,2,3],10)
print(s.linear())

right = len(data)-1
left = 0
while left < right:
    mid = right/2
    break
