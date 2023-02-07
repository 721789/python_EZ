# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:58:45 2023

@author: PREETHI
"""

#prime number
num=int(input())
flag = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num//2):
        #for i in range(2, sqrt(num))
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")