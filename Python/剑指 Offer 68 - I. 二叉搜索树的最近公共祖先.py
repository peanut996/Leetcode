#!/usr/bin/python3.7
# 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
# from typing import List
from DataStructure import TreeNode
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val <= root.val <= p.val or q.val >= root.val >= p.val:
            return root
        elif q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)