# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:24:00 2023

@author: PREETHI
"""

from test import Node

class LL:
    def addEle(self,head,val):
        newNode=Node(val)  #object created for class Node
        cur=head
        while cur.addr!=Node:
            cur=cur.addr
        cur.addr=newNode
    def print_list(self,head):
         cur=head
         while cur!=None:
             
             print(f'{cur.data}',end="->")
             cur=cur.addr
        
    def removeEle(self,head,data):
        prev=None
        cur=head
        while cur.data!=None:
             prev=cur
             cur=cur.addr
             if cur.data=val and c=!=0:
                  prev.addr=cur.addr
           
             
       
       
        
ob=LL()
head=Node(10)
ob.addEle(head,20)
ob.addEle(head,20)
ob.addEle(head,30)
ob.addEle(head,40)
ob.addEle(head,30)
ob.addEle(head,40)
ob.removeEle(head,40)
ob.print_list(head)

