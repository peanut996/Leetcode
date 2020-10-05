#!/usr/bin/python3.7
# 剑指 Offer 32 - I. 从上到下打印二叉树
from typing import List
from DataStructure import TreeNode
# from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        # 特判
        if not root: return []
        queue,res = [root],[]
        while queue:
            tmp = queue[0]
            res.append(tmp.val)
            queue = queue[1:]
            if tmp.left: queue.append(tmp.left)
            if tmp.right: queue.append(tmp.right)
        return res
        

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
