#!/usr/bin/python3.7
# 剑指 Offer 32 - III. 从上到下打印二叉树 III
from typing import List
from DataStructure import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 可使用双端队列 判断len(res)确定奇偶层
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
        # 处理倒序输出
        for i,v in enumerate(res):
            if i%2 == 1:
                res[i]=res[i][::-1]
        return res



if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
