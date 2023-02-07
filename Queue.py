# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:03:03 2023

@author: PREETHI
Queue implementation
"""
class Queue:
    l=[]
    def enQ(self,a):
        self.l.append(a)
    def deQ(self):
        self.l.pop(0)
    def topele(self):
        print(self.l[r])
    def siez(self):
        print("seze of the queue is",len(self.l))
ob=Queue()
ob.enQ(10)
ob.enQ(20)
ob.enQ(30)
print(ob.l)
ob.deQ()
print(ob.l)

