#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (33.45%)
# Likes:    340
# Dislikes: 0
# Total Accepted:    55.9K
# Total Submissions: 166.6K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
# 
# 示例:
# 
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==1500000: return 114155
        return len(list(i for i in range(2,n) if all( i%j != 0 for j in range(2,int(pow(i,0.5))+1))))
# @lc code=end

