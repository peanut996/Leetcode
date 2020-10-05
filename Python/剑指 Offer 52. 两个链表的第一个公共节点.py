#!/usr/bin/python3.7
# 剑指 Offer 52. 两个链表的第一个公共节点
# from typing import List
from DataStructure import ListNode
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptrA,ptrB = headA,headB
        while ptrA !=ptrB:
            ptrA = ptrA.next if ptrA else headA
            ptrB = ptrB.next if ptrB else headB
        return ptrA

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
