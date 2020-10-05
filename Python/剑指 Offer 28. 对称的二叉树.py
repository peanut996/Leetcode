#!/usr/bin/python3.7
# 剑指 Offer 28. 对称的二叉树
# from typing import List
from DataStructure import TreeNode
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left: TreeNode, right: TreeNode) -> bool:
            # 两个空节点
            if not left and not right: return True
            # 非对称叶子节点
            if (left and not right) or (right and not left): return False
            # 判断值 递归 下一层节点是否对称
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        # root是否为空
        if not root :return True
        return dfs(root.left, root.right)


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
