#!/usr/bin/python3.7

"""1248. Count Number of Nice Subarrays
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。

示例：
输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
"""
from typing import List
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = [ 0 ] * (len(nums) + 1)
        # 基准线 odd=k时 等于1
        cnt[0] = 1
        res,odd = 0,0
        for num in nums:
            if num&1 == 1:
                odd+=1
            if odd >= k:
                res+=cnt[odd-k]
            cnt[odd]+=1
        return res

if __name__ == '__main__':
    try:
        assert exec
    except AssertionError:
        print('解答错误')
