#!/usr/bin/python3.7
# 剑指 Offer 57. 和为s的两个数字
from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    left,right = 0,len(nums)-1
    while left < right:
        if nums[left]+nums[right] == target:
            return [nums[left],nums[right]]
        elif nums[left]+nums[right] < target:
            left += 1
        else:
            right -=  1
    return []

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')


