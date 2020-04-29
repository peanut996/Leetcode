#!/usr/bin/python3.7

"""23. Merge k Sorted Lists
"""

from typing import List
from DataStructure import ListNode
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        val_list=[]
        head = curr = ListNode(0)
        for l in lists:
            while l:
                val_list.append(l.val)
                l=l.next
                

        for v in sorted(val_list):
            curr.next = ListNode(v)
            curr = curr.next
        return head.next



if __name__ == '__main__':
    solution = Solution()
    lists = [ListNode(0)]
    print(solution.mergeKLists(lists))
    try:
        assert exec
    except AssertionError:
        print('解答错误')
