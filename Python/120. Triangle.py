#!/usr/bin/python3.7
from typing import List
# 120. 三角形最小路径和

# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

#  

# 例如，给定三角形：

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

#  

# 说明：

# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/triangle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #  无法优化的dfs
        # length = len(triangle)-1
        # res = []
        # def dfs(sum,index,k):
        #     if k>length: return
        #     elif k==length:
        #         res.append(sum+triangle[k][index])
        #     else:
        #         dfs(sum+triangle[k][index],index,k+1)
        #         dfs(sum+triangle[k][index],index+1,k+1)
        # dfs(0,0,0)
        # return min(res)
        max_depth = len(triangle)
        memo = dict()
        def dfs(depth: int,index: int) -> int:
            if depth == max_depth: return 0
            if (depth,index) in memo.keys():
                return memo[(depth,index)]
            memo[(depth,index)] = min(dfs(depth+1,index),dfs(depth+1,index+1))+triangle[depth][index]
            return memo[(depth,index)]
        return dfs(0,0)


if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
