# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:19:40 2023

@author: PREETHI
"""
#stack implementation
class Stack:
    top=0
    l=[]
    def push(self,a):
        self.l.append(a)
        self.top+=1
    def pop(self):
        print("element removed",self.l.pop())
        self.top-=1
        
    def size(self):
        print("size of stack is",len(self.l))
    def stack_peek(self):
       print("the top elemet is",self.l[-1])
obj=Stack()
obj.push(10)
obj.push(20)
obj.push(30)
print(obj.l)
obj.pop()
print(obj.l)
obj.stack_peek()
obj.size()

        