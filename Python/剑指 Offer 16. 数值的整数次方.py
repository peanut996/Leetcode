#!/usr/bin/python3.7
# 剑指 Offer 16. 数值的整数次方
# from typing import List

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂 二分思想 粒度从x变为x^2
        if not x: return 0
        if n<0: x,n = 1/x,-n
        res = 1
        while n:
            if n&1: res *= x
            x*=x
            n >>= 1
        return res

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
