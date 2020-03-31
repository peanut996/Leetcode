#!/usr/bin/python3.7
"""206.Reverse Linked List

反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

warning: 此脚本不可运行
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        queue=[]
        node=head
        while head is not None:
            queue.append(head.val)
            head=head.next
        head=node
        while head is not None:
            head.val=queue.pop()
            head=head.next
        return node


def main():
    try:
        assert exec
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
