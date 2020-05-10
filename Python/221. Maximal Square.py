#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (39.67%)
# Likes:    334
# Dislikes: 0
# Total Accepted:    36.4K
# Total Submissions: 90K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        row, col, res = len(matrix), len(matrix[0]), 0
        dp = [ [0]*(col+1) for _ in range(row+1) ]
        for r in range(1,row+1):
            for c in range(1,col+1):
                if matrix[r-1][c-1] == '1':
                    # 状态转移方程 参见木桶效应
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])+1
                    res = max(res,dp[r][c])
        return res*res

# @lc code=end

