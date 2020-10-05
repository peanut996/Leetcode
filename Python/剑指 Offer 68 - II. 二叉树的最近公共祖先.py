#!/usr/bin/python3.7
# 剑指 Offer 68 - II. 二叉树的最近公共祖先
# from typing import List
from DataStructure import TreeNode
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """后序遍历dfs 
            通过判断左右叶子节点向上返回值判定深度最大的祖先
        """
        
        if not root or root.val == q.val or root.val == q.val: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left: return right
        if not right: return left
        return root


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
