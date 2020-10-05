#!/usr/bin/python3.7
# 剑指 Offer 15. 二进制中1的个数
# from typing import List



class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        while n:
            # res += n&1
            # n>>=1
            res += 1
            n &= (n - 1)
        return res
