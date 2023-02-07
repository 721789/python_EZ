# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:38:12 2023

@author: PREETHI
"""

a=int(input())
print(a,end=" ")
while(True):
    if a%2==0:
        a=a//2
        print(a,end=" ")
    else:
        a=3*a+1
        print(a,end=" ")
    if a==1:
        break
    