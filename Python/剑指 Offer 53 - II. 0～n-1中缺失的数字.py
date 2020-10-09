#!/usr/bin/python3.7
# 剑指 Offer 53 - II. 0～n-1中缺失的数字
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        while left <= right:
            # 注意位运算的优先级问题
            mid = left + ((right - left)>>1)
            if nums[mid] == mid:
                left = mid+1
            else:
                right = mid-1
        return left

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
