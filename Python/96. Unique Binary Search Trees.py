#!/usr/bin/python3.7

# from typing import List
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = list( 0 for i in range(n+1))
        dp[0], dp[1] =1, 1
        # for i in range(2,n+1):
        #     for j in range(1, i+1):
        #         dp[i] += dp[j - 1] * dp[i-j]
        # return dp[n]

if __name__ == '__main__':
    n = 3
    solution = Solution()
    try:
        assert solution.numTrees(n) == 5
    except AssertionError:
        print('解答错误')