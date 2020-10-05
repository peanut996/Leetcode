#!/usr/bin/python3.7
# 剑指 Offer 56 - I. 数组中数字出现的次数
from typing import List
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        xor,mask = 0, 1
        a,b = 0,0
        for num in nums: xor ^= num
        # 获取区分的1的位置
        while not mask&xor:
            mask <<= 1
        for num in nums:
            if num & mask :
                a ^= num
            else:
                b ^= num
        return [a,b]

