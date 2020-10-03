#!/usr/bin/python3.7

from typing import List
# 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
def exchange(self, nums: List[int]) -> List[int]:
    length = len(nums)
    for i in nums[:length]: 
        if i%2 != 0:
            nums.append(i)
    for i in nums[:length]: 
        if i%2 == 0:
            nums.append(i)
    return nums[length:]

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
