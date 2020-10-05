#!/usr/bin/python3.7
# 剑指 Offer 24. 反转链表
# from typing import List
from DataStructure import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 双指针法
        cur,pre = head,None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 注意这里的节点应该是后节点
        return pre

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
