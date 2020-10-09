#!/usr/bin/python3.7
# 剑指 Offer 26. 树的子结构
# from typing import List
from DataStructure import TreeNode
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B: return False        
        def helper(A,B):
            if not B: return True
            if not A: return False
            return A.val==B.val and helper(A.left,B.left) and helper(A.right,B.right)
        return helper(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
