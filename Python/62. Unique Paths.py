#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# https://leetcode-cn.com/problems/unique-paths/description/
#
# algorithms
# Medium (60.72%)
# Likes:    587
# Dislikes: 0
# Total Accepted:    116.2K
# Total Submissions: 191K
# Testcase Example:  '3\n2'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 问总共有多少条不同的路径？
# 
# 
# 
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
# 
# 
# 
# 示例 1:
# 
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 
# 
# 示例 2:
# 
# 输入: m = 7, n = 3
# 输出: 28
# 
# 
# 
# 提示：
# 
# 
# 1 <= m, n <= 100
# 题目数据保证答案小于等于 2 * 10 ^ 9
# 
# 
#

# @lc code=start
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DFS 暴力递归

        # 动态规划
        dp = [ [0] * m for _ in range(n) ]
        for i in range(n):
            for j in range(m):
                # print(i,j)
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[-1][-1]

        # 排列组合
        # C(m+n-2, m-1)
        # return int(math.factorial(m + n- 2) / math.factorial(m - 1) / math.factorial(n - 1))

# @lc code=end

