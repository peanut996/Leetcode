#!/usr/bin/python3.7
"""322. Coin Change
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例：
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """动态规划
        """
        dp=[float('inf') for i in range(amount+1)]
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin<0: continue
                dp[i]=min(dp[i],dp[i-coin]+1)
        return  dp[amount] if dp[amount]!=float('inf') else -1


def main():
    solution = Solution()
    coins,amount=[1,2,5],11
    try:
        assert solution.coinChange(coins,amount)==3
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
