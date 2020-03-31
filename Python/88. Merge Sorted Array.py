#!/usr/bin/python3.7
"""88. Merge Sorted Array
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

示例：
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=sorted(nums1[:m]+nums2)
        

def main():
    solution = Solution()
    nums1,nums2=[1,2,3,0,0,0],[2,5,6]
    solution.merge(nums1,3,nums2,3)
    print(nums1)
    try:
        assert nums1==[1,2,2,3,5,6]
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
