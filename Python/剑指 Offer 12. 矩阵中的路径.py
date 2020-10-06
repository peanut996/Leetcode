#!/usr/bin/python3.7
# 剑指 Offer 12. 矩阵中的路径
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row: int, col: int, k: int)-> bool:
            # 剪枝
            if not 0 <= row <len(board) or not 0 <= col <len(board[0]) or board[row][col]!=word[k]:
                return False
            # 判断是否匹配完成
            if k==len(word)-1: return True
            # 回溯 临时标记为不可访问状态
            tmp,board[row][col] = board[row][col],'#'
            res = dfs(row+1,col,k+1) or dfs(row-1,col,k+1) or dfs(row,col+1,k+1) or dfs(row,col-1,k+1)
            # 还原状态
            board[row][col] = tmp
            return res

        for row in range(len(board)):
            for col in range(len(board[row])):
                if dfs(row,col,0): return True
        return False
        
            
            


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    solution = Solution()
    try:
        assert solution.exist(board,'ABCCED') == True
        print('解答正确')
    except AssertionError:
        print('解答错误')
