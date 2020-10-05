#!/usr/bin/python3.7
# 剑指 Offer 64. 求1+2+…+n
# from typing import List
class Solution:
    def sumNums(self, n: int) -> int:
        return self.sumNums(n-1) + n if n>=0 else 0


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
