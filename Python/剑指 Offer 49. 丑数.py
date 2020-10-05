#!/usr/bin/python3.7

# from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        a,b,c,dp = 0,0,0,[1] * n
        for i in range(1,n):
            n2,n3,n5 = dp[a]*2,dp[b]*3,dp[c]*5
            dp[i] = min(n2,n3,n5)
            if dp[i] == n2: a+=1
            if dp[i] == n3: b+=1
            if dp[i] == n5: c+=1
        return dp[-1]

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
