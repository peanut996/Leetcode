#!/usr/bin/python3.7

# from typing import List

# LCP 19. 秋叶收藏集
# 动态规划 

def minimumOperations(self, leaves: str) -> int:
    dp = [ [0,0,0] for i in range(len(leaves))]
    def isYellow(leave): return leave=='y'
    def isRed(leave): return leave=='r'
    # 0 1 2 表示叶子状态
    # 记录 已知状态数组元素：
    #     1、第一个叶子，必须是左半部分，所以只需判断是不是 黄色叶子 即可
    #     2、第一个叶子，必须是左半部分，所以 state[0][1] 和 state[0][2] 都是无效的
    #     3、第二个叶子，可以是左半部分，也可以是中间部分，但是不能是右半部分(每个区间必须有叶子)，
    #         因此 state[1][2]是无效的
    dp[0][0] = isYellow(leaves[0])
    dp[0][0],dp[0][1],dp[0][2] = float('inf'),float('inf'),float('inf')

    for i in range(1,len(leaves)):
        dp[i][0] = dp[i-1][0] + isYellow(leaves[i])
        dp[i][1] = min(dp[i-1][0],dp[i-1][1]) + isRed(leaves[i])
        if i > 1:
            dp[i][2] = min(dp[i-1][1],dp[i-1][2]) + isYellow(leaves[i])

    return dp[len(leaves)-1][2]

    


        

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
