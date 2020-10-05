#!/usr/bin/python3.7
# 剑指 Offer 42. 连续子数组的最大和
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 注意这里的dp初始值与后面range循环次数的关系
        # n,dp,m = len(nums),0,nums[0]
        # for i in range(n):
        #     dp = max(dp+nums[i],nums[i])
        #     m = max(dp,m)
        # return m

        # 直接修改 空间复杂度O(1)
        for i in range(1,len(nums)):
            nums[i]+=max(0,nums[i-1])
        return max(nums)





if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
