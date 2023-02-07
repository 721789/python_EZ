# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:45:47 2023

@author: PREETHI
Queue implementation using Stack
"""
class Queue_Stack:
    s1=[]
    s2=[]
    def enqueue(self,a):
        self.s1.append(a)
        print("element added",self.s1)
        
    def dequeue(self):
        while len(self.s1):
            self.s2.append(self.s1.pop())
        print("element removed is ",self.s2.pop())
        while(len(self.s2)):
            self.s1.append(self.s2.pop())
ob= Queue_Stack()
ob.enqueue(10)
ob.enqueue(20)
ob.enqueue(30)
print(ob.s1)
ob.dequeue()
print(ob.s1)
        
    
        
    

