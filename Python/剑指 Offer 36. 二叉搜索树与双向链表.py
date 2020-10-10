#!/usr/bin/python3.7
# 剑指 Offer 36. 二叉搜索树与双向链表
# from typing import List
from DataStructure import Node
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur: Node):
            if not cur: return None
            dfs(cur.left)
            if self.pre:
                self.pre.right,cur.left =cur,self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)
        if not root: return None
        self.pre=None
        dfs(root)
        self.head.left,self.pre.right = self.pre,self.head
        return self.head

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
