# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:19:55 2019

@author: Thangarajan
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head == None:
            node = Node(data)
            node.next = None
            print(node.data)
            return node.data
        else:
            node = Node(data)
            print(head)
            node.next = None
            return node.next
        
    #Complete this method

mylist= Solution()
head=None
for i in [1,2,3,4]:
    data=i
    head=mylist.insert(head,data)    
mylist.display(head);