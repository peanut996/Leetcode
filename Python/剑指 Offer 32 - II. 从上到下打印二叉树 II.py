#!/usr/bin/python3.7
# 剑指 Offer 32 - II. 从上到下打印二叉树 II
from typing import List
from DataStructure import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue,res = [root],[]
        while queue:
            tmp_list = []
            tmp_queue = queue
            queue = []
            while tmp_queue:
                tmp_node = tmp_queue[0]
                tmp_queue = tmp_queue[1:]
                tmp_list.append(tmp_node.val)
                if tmp_node.left: queue.append(tmp_node.left)
                if tmp_node.right: queue.append(tmp_node.right)
            res.append(tmp_list)
        return res
