#!/usr/bin/python3.7

from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        num_zero,ret,index = 0,0,0
        while not nums[index]:
            num_zero+=1
            index+=1
        while index < len(nums):
            if index+1<len(nums) and nums[index+1] == nums[index]: return False
            if index+1<len(nums) and nums[index+1] != nums[index]+1: ret += nums[index+1]-nums[index]-1
            index+=1
        return not ret or num_zero >= ret 
        
if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
