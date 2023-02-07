# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:21:05 2023

@author: PREETHI
"""

s1=[1,2,3,4,5]
s2=[6,7,8,9,10]
s3=[]
for i in range(len(s2)):
    s3.append(s2.pop())
for i in range(len(s3)):
    s1.append(s3.pop())
for i in range(len(s1)):
    print(s1[i],end=" ")