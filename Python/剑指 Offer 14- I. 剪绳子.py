#!/usr/bin/python3.7
# 剑指 Offer 14- I. 剪绳子
# from typing import List
import math
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 数学做法
        # if n <= 3: return n - 1
        # a, b = n // 3, n % 3
        # if b == 0: return int(math.pow(3, a))
        # if b == 1: return int(math.pow(3, a - 1) * 4)
        # return int(math.pow(3, a) * 2)

        # 动态规划
        # 1，j和i-j都不能再拆了
        # dp[i]=j*(i-j);
        # 2，j能拆，i-j不能拆
        # dp[i]=dp[j]*(i-j);
        # 3，j不能拆，i-j能拆
        # dp[i]=j*dp[i-j];
        # 4，j和i-j都能拆
        # dp[i]=dp[j]*dp[i-j];

        
        dp = [0] * (n+1)
        dp[0],dp[1]=0,1
        for i in range(2,n+1):
            for j in range(1,i//2+1): # 因为对称可以优化i//2
                # 状态转移
                dp[i] = max(dp[i],max(j,dp[j])*max(i-j,dp[i-j]))
        return dp[-1]


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')

# 作者：sdwwld
# 链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/shu-xue-zhi-shi-he-dong-tai-gui-hua-liang-chong-fa/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。