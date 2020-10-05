#!/usr/bin/python3.7
# 剑指 Offer 65. 不用加减乘除做加法
# from typing import List
class Solution:
    def add(self, a: int, b: int) -> int:
        # python 负数需先限定至32位无符号
        x = 0xffffffff
        a,b = a&x,b&x
        while b:
            # carry = (a&b) << 1 & x
            # a ^=b
            # b = carry
            a,b = a^b, (a & b) << 1 & x
        # 补码为负数情况
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
