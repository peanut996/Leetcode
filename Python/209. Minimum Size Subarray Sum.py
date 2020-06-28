#!/usr/bin/python3.7
"""209. Minimum Size Subarray Sum
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""
# from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s: return 0
        res = float('inf')
        left, right, cursum = 0, 0, 0
        # 滑动窗口
        # 先扩张
        while right < len(nums):
            cursum += nums[right]

            while cursum >= s:
                res = min(res, right - left + 1)
                cursum -= nums[left]
                # 收缩
                left += 1
            right += 1
        return res


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
