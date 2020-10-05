#!/usr/bin/python3.7
# 剑指 Offer 27. 二叉树的镜像
# from typing import List

from DataStructure import TreeNode

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return root
        root.left,root.right = root.right,root.left
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
