#!/usr/bin/python3.7
# 剑指 Offer 07. 重建二叉树
from typing import List
from DataStructure import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 判定是否遇到叶子节点
        if not (preorder and inorder):
            return None
        root = TreeNode(preorder[0])
        # 获取中序数组中root下标
        root_index = inorder.index(root.val)
        # 注意这里的中序数组root下标恰好也是前序数组左右子树的分界线
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        return root


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
