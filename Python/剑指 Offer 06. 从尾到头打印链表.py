#!/usr/bin/python3.7
# 剑指 Offer 06. 从尾到头打印链表
from DataStructure import ListNode
from typing import List

def reversePrint(self, head: ListNode) -> List[int]:
    res = []
    guard = head
    while guard:
        res.append(guard.val)
        guard=guard.next
    return res[::-1]


if __name__ == '__main__':
    try:
        print('Hello World')
    except AssertionError:
        print('解答错误')
