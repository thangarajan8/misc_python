# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 17:36:16 2019

@author: Thangarajan
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
        
class double_ll:
    
    def __init__(self):
        self.head = None
        
    def insert(self,newNode):
        if self.head is None:
            print('list is empty so we are going to add the node as head node')
            self.head= newNode
        else:
            print('list is not empty now we have to connect')
            lastNode = self.head
            while True:
                if lastNode.next is None and lastNode.prev is None:
                    break
                lastNode = lastNode.next
            print(lastNode.data)
            if lastNode.next is None and lastNode.prev is None:
                lastNode.next = newNode
                lastNode.prev = self.head
            else:
                lastNode.next = newNode
                lastNode.prev = lastNode.prev
            
#                    
                    
n1 = Node('thanga')
n2 = Node('vini')
n3 = Node('ammu')
dll = double_ll()
dll.insert(n1)
dll.insert(n2)
dll.insert(n3)
