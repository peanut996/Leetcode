#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
from typing import List
import collections
# @lc code=startclass Solution:
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        pre_mod = 0  # 存储当前位置的上一个位置的前缀和的余数加上当前位置的值对K的余数
        presum_count = collections.defaultdict(int)
        presum_count[0] = 1
        for i in range(len(A)):
            pre_mod = (pre_mod + A[i]) % K
            # 下面这行感觉最不好理解
            res += presum_count[pre_mod]  # 如果能在dict中找到相同的pre_mod，说明当前节点前的某个位置的前缀和到当前位置的前缀和间存在若干个K
            presum_count[pre_mod] += 1
        return res
# @lc code=end