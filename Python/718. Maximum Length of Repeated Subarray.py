#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (50.41%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    22.7K
# Total Submissions: 43.1K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 示例 1:
# 
# 
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释: 
# 长度最长的公共子数组是 [3, 2, 1]。
# 
# 
# 说明:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # 查询相同数量的序列
        def findmaxlength(addA: int, addB, length):
            res = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    res = max(res, k)
                else:
                    k = 0
            return res

        res , lengthA, lengthB = 0, len(A), len(B)
        
        # A,B对齐 
        for i in range(lengthA):
            length = min(lengthB, lengthA - i)
            res = max(res, findmaxlength(i, 0, length))
        for i in range(lengthB):
            length = min(lengthA, lengthB - i)
            res = max(res, findmaxlength(0, i, length))
        return res
        
# @lc code=end

