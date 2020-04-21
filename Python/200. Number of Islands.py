#!/usr/bin/python3.7

"""200. Number of Islands
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1:

输入:
11110
11010
11000
00000
输出: 1
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])
        res = 0
        # dfs 解法
        # def dfs(i,j):
        #     """访问一个岛屿 并标记
        #     """
        #     grid[i][j] = '0'
        #     for x,y in directions:
        #         x_t = i+x
        #         y_t = j+y
        #         if 0 <= x_t < row and 0 <= y_t < col and grid[x_t][y_t] == '1':
        #             dfs(x_t,y_t)
        
        # for i in range(row):
        #     for j in range(col):
        #         if grid[i][j] == '1':
        #             res+=1
        #             dfs(i,j)
        
        return res






if __name__ == '__main__':
    try:
        assert exec
    except AssertionError:
        print('解答错误')
