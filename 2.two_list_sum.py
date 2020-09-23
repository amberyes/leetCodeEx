#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' leetCode02 '
import sys

__author__='Amber Ye'

# 定义节点
class ListNode:

    def __init__(self,x):
        self.value=x
        self.next=None

# 定义链表
class LinkList:

    def __init__(self):
        self.head=None

    # 建立链表
    def initList(self,data):
        self.head=ListNode(data[0])
        r=self.head
        p=self.head
        for i in data[1:]:
            node=ListNode(i)
            p.next=node
            p=p.next
        return r

    # 打印链表元素，每个元素后接空格
    def printList(self,head):
        if head is None:return
        node=head
        while node != None:
            print(node.value,end=" ")
            node=node.next

class Solution:
    def twoSum(self,L1,L2):
        temp=ListNode(0)
        L3=temp
        a=0
        while L1!=None or L2!=None or a!=0 :
            if L1!=None:
                a+=L1.value
                L1=L1.next
            if L2!=None:
                a+=L2.value
                L2=L2.next
            temp.next=ListNode(a%10)
            temp=temp.next
            a=a//10
        return L3.next

if __name__=='__main__':
    line1=sys.stdin.readline().strip()
    l3=list(map(int,line1.split()))
    line2=sys.stdin.readline().strip()
    l4=list(map(int,line2.split()))

    b=LinkList()
    l1=b.initList(l3)
    l2=b.initList(l4)
    a=Solution()
    l5=a.twoSum(l1,l2)
    b.printList(l5)





