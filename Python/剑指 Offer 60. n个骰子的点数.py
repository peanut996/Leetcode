#!/usr/bin/python3.7
# 剑指 Offer 60. n个骰子的点数
from typing import List
class Solution:
    def twoSum(self, n: int) -> List[float]:
        # 递归
        # base,nums = float(1/6),[float(1/6)]*(6*n)
        # if n==1 : return nums 
        # pre = self.twoSum(n-1)
        # cur = [0 for _ in range(5*n + 1)]
        # for i in range(len(pre)):
        #     for j in range(1,7):
        #         # 从n-1结果推到n
        #         cur[j-1+i] += pre[i]*base
        # return cur
        # 动态规划
        base = float(1/6)
        dp = [ [0 for _ in range(6*n+1)] for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = float(1/6)
        for i in range(2,n+1):
            for j in range(i,6*i+1):
                for k in range(1,7):
                    # i表示多少个骰子，j表示点数之和，k表示骰子数字
                    if j-k<0: break
                    dp[i][j]+=dp[i-1][j-k]*base
        # 去除0的点数
        return dp[n][n:6*n+1]

        


if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
