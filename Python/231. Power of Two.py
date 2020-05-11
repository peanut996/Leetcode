#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (47.98%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    58.3K
# Total Submissions: 121.5K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        恒有 n & (n - 1) == 0，这是因为：
        n 二进制最高位为 11，其余所有位为 0；
        n - 1 二进制最高位为 0，其余所有位为 1；
        """

        return n > 0 and n & (n - 1) == 0
# @lc code=end

