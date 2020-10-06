#!/usr/bin/python3.7
# 剑指 Offer 63. 股票的最大利润
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0表示不持有股票，1表示持有股票
        i_0,i_1 = 0,-float('inf')
        for i in range(len(prices)):
            # 状态转移
            # 当天不持有股票则前一天不持有或者今天卖出
            i_0=max(i_0,i_1+prices[i])
            # 当天持有则前一天已持有或者当天买入
            i_1=max(i_1,-prices[i])
        return i_0

        # 另一种动态规划 本质是等价的
        # cost, profit = float("+inf"), 0
        # for price in prices:
        #     cost = min(cost, price)
        #     profit = max(profit, price - cost)
        # return profit

        # 作者：jyd
        # 链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/solution/mian-shi-ti-63-gu-piao-de-zui-da-li-run-dong-tai-2/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
