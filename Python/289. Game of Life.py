#!/usr/bin/python3.7
"""289. Game of Life
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

    如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
    如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
    如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
    如果死细胞周围正好有三个活细胞，则该位置死细胞复活；

根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
"""
import copy
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board)-1,len(board[0])-1
        directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        # 这里复制了数组 可采用其他数字标识复合状态如2,3在&1得出最后的结果修改原数组
        List=copy.deepcopy(board)
        for r,row in enumerate(board):
            for c,v in enumerate(row):
                alive=0
                for (i,j) in directions:
                    if 0<=r+i<=m and 0<=c+j<=n and board[r+i][c+j]:
                        alive+=1
                if v==1 and  (alive<2 or alive>3):
                    List[r][c]=0
                if v==0 and alive==3:   
                    List[r][c]=1
        board[:]=List


def main():
    solution = Solution()
    board=[[0,1,0], 
           [0,0,1],
           [1,1,1],
           [0,0,0]]
    solution.gameOfLife(board)
    print(board)
    try:
        assert board==[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
