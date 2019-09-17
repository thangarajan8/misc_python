# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:36:13 2019

@author: Thangarajan
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,newNode):
        if self.head is None:
            print('None')
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def printlist(self):
        lastNode = self.head
        print('Head Node '+lastNode.data)
        while True:
            print(lastNode.data)
            if lastNode.next is None:
                break
            lastNode = lastNode.next
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
n1 = Node('thanga')
n2 = Node('Vini')
n3 = Node('Ammu')
ll = LinkedList()
ll.insert(n1)
ll.insert(n2)
ll.insert(n3)
ll.printlist()
ll.isEmpty()
