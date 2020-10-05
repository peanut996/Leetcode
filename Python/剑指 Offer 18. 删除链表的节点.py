#!/usr/bin/python3.7
# 剑指 Offer 18. 删除链表的节点
# from typing import List
from DataStructure import ListNode
def deleteNode(self, head: ListNode, val: int) -> ListNode:
    cur = ListNode(0)
    cur.next = head
    res = cur
    
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        cur = cur.next
    return res.next

if __name__ == '__main__':
    try:
        assert exec
    except AssertionError:
        print('解答错误')
