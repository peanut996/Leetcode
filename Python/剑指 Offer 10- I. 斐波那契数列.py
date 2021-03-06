#!/usr/bin/python3.7

# from typing import List

class Solution:
    def fib(self, n: int) -> int:
        # dp = [0] * (n+1)
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n] % 1000000007
        # 空间复杂度O(1) 算法
        a,b = 0,1
        for _ in range(n):
            a,b = b,a+b
        return a % 1000000007