#!/usr/bin/python3.7
# 剑指 Offer 03. 数组中重复的数字
from typing import List

def findRepeatNumber(self, nums: List[int]) -> int:
        # nums_list = [0] *  len(nums)
        # for i in nums:
        #     nums_list[i] += 1
        # for i,v in enumerate(nums_list):
        #     if v > 1: return i
        # return -1

        # 原地交换 因为数值限定于n-1内所以只要交换遇到冲突 即遇到了重复值
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i+=1
                continue
            if nums[i] == nums[nums[i]]: return nums[i]
            # nums[i],nums[nums[i]] = nums[nums[i]],nums[i] 错误写法 先赋值了nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1



if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
