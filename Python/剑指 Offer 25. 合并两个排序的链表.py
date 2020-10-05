#!/usr/bin/python3.7
# 剑指 Offer 25. 合并两个排序的链表
# from typing import List
from DataStructure import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        res = head
        while l1 and l2:
            if l1.val < l2.val:
                head.next,l1 = l1,l1.next
            else:
                head.next,l2 = l2,l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return res.next

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
