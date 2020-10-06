#!/usr/bin/python3.7
# 剑指 Offer 62. 圆圈中最后剩下的数字
# from typing import List

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 约瑟夫环
        res = 0
        for i in range(2,n+1):
            res = (res + m)%i
        return res

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
