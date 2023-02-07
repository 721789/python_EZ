# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:09:18 2023

@author: PREETHI
Parenthesis matching
"""
stack=[]
s="(()())"
for i in s:
    if i=='(':
        stack.append(i)
    else:
        if len(stack)==0:
            print("unbalanced")
            break
        stack.pop()
        
if len(stack)==0:
    print("balanced string")
else:
    print("unbalanced string")
        
        
