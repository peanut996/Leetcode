#!/usr/bin/python3.7
# 剑指 Offer 35. 复杂链表的复制
# from typing import List
# TODO 原地修改空间O(1)
from DataStructure import Node
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # dfs借助Hash表做法
        # dic = dict()
        # def dfs(head: 'Node'):
        #     if not head: return None
        #     if head in dic: return dic[head]
        #     copy  = Node(head.val)
        #     dic[head] = copy
        #     copy.next = dfs(head.next)
        #     copy.random = dfs(head.random)
        #     return copy
        # return dfs(head)

        # 都是利用哈希表
        dic =dict()
        dic[None]=None
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur=cur.next
        cur = head
        while cur:
            dic[cur].next = dic[cur.next]
            dic[cur].random = dic[cur.random]
            cur=cur.next
        return dic[head]


if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
