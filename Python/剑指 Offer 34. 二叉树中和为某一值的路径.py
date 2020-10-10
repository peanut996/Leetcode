#!/usr/bin/python3.7
# 剑指 Offer 34. 二叉树中和为某一值的路径
from typing import List
from DataStructure import TreeNode

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def dfs(root: TreeNode,sum: int,tmp: List[int]):
            if not root: return
            # 注意这里的数组引用问题
            tmp = list(tmp)
            tmp.append(root.val)
            if not root.left and not root.right and root.val == sum: 
                res.append(tmp)
            else:
                dfs(root.left,sum - root.val,tmp)
                dfs(root.right,sum - root.val,tmp)
        dfs(root,sum,[])
        return res


if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
