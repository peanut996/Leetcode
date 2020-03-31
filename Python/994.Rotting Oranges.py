#!/usr/bin/python3.7
"""994.Rotting Oranges
在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

示例：
输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
"""

from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """BFS
        """
        row,col,time=len(grid),len(grid[0]),0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        #烂桔子入栈
        queue=[(i,j,time) for i in range(row) for j in range(col) if grid[i][j]==2]

        #BFS
        while queue:
            i,j,time=queue.pop(0)
            # print('-----------第'+str(time)+'轮------------------')
            # print('现在是('+str(i)+','+str(j)+')'+'桔子')
            for di,dj in directions:
                if 0<=di+i<row and 0<=dj+j<col and grid[di+i][dj+j]==1 :
                    grid[di+i][dj+j]=2
                    # print('桔子('+str(i+di)+','+str(j+dj)+')'+'可被感染')
                    queue.append((di+i,dj+j,time+1))

        #判断是否还有新鲜桔子
        for row in  grid :
            if 1 in row:
                return -1
        
        return time


def main():
    grid=[[2,1,1],[1,1,0],[0,1,1]]
    solution=Solution()
    assert solution.orangesRotting(grid)==4


if __name__ == '__main__':
    main()