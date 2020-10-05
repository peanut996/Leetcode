#!/usr/bin/python3.7
# 剑指 Offer 47. 礼物的最大价值
from typing import List

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # 状态转移方程
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0: continue
                if i==0: grid[i][j] += grid[i][j-1]
                elif j==0: grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += max(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]

        # 可提前优化 i==0 or j==0的一行一列
        # m, n = len(grid), len(grid[0])
        # for j in range(1, n): # 初始化第一行
        #     grid[0][j] += grid[0][j - 1]
        # for i in range(1, m): # 初始化第一列
        #     grid[i][0] += grid[i - 1][0]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        # return grid[-1][-1]

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
