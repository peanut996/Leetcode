#!/usr/bin/python3.7
# 剑指 Offer 54. 二叉搜索树的第k大节点
# from typing import List
from DataStructure import TreeNode
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        nums = []
        def inorder(root: TreeNode):
            if not root: return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return nums[-k]


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
