#!/usr/bin/python3.7
# 剑指 Offer 55 - I. 二叉树的深度
# from typing import List
from DataStructure import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
