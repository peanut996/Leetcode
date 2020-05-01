#!/usr/bin/python3.7

# from typing import List

"""21. Merge Two Sorted Lists
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

from DataStructure import ListNode
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 迭代
        # head = ListNode(0)
        # res = head
        # while l1 is not None and l2 is not None:
        #     if l1.val < l2.val:
        #         head.next = l1
        #         l1=l1.next
        #         head=head.next
        #     else:
        #         head.next = l2
        #         l2 = l2.next
        #         head=head.next
        # while l1 is not None:
        #     head.next = l1
        #     l1=l1.next
        #     head=head.next
        # while l2 is not None:
        #     head.next = l2
        #     l2=l2.next
        #     head=head.next
        # return res.next

        # 递归
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2




        


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
