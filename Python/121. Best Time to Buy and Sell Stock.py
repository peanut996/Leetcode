#!/usr/bin/python3.7
"""121. Best Time to Buy and Sell Stock
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例：
输入: [7,1,5,3,6,4]
输出: 5
"""
"""
解析参见：https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/tuan-mie-gu-piao-wen-ti
base case：
dp[-1][k][0] = dp[i][0][0] = 0
dp[-1][k][1] = dp[i][0][1] = -infinity

状态转移方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

"""

"""本题k=1
dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i]) 
            = max(dp[i-1][1][1], -prices[i])
解释：k = 0 的 base case，所以 dp[i-1][0][0] = 0。

现在发现 k 都是 1，不会改变，即 k 对状态转移已经没有影响了。
可以进行进一步化简去掉所有 k：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], -prices[i])
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i_0,i_1=0,-float('inf')
        for i in range(len(prices)):
            #dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            i_0=max(i_0,i_1+prices[i])
            #dp[i][1] = max(dp[i-1][1], -prices[i])
            i_1=max(i_1,-prices[i])
        return i_0

def main():
    solution = Solution()
    prices=[7,1,5,3,6,4]
    try:
        assert solution.maxProfit(prices)==5
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
