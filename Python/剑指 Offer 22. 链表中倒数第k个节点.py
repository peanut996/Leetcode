#!/usr/bin/python3.7
# 剑指 Offer 22. 链表中倒数第k个节点
# from typing import List

from DataStructure import ListNode
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # res = []
        # while head:
        #     res.append(head)
        #     head=head.next
        # return res[-k]

        # 快慢指针 快指针先走k步
        slow=fast=head
        for _ in range(k):
            if not fast: return
            fast=fast.next
        while fast:
            fast,slow=fast.next,slow.next
        return slows
        


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
