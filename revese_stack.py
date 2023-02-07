# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:45:08 2023

@author: PREETHI 
reverseing a stack"""
stack1=[10,20,30,40]
stack2=[]
for i in range(len(stack1)):
    e=stack1.pop()
    stack2.append(e)


print(stack1)
print(stack2)
for i in range(len(stack2)):
    print(stack2.pop(),end=" ")


