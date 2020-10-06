#!/usr/bin/python3.7
# 剑指 Offer 14- II. 剪绳子 II
# from typing import List

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return 3 ** a % 1000000007
        if b == 1: return 3**(a-1)*4 % 1000000007
        return 3**a*2 % 1000000007

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
