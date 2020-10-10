#!/usr/bin/python3.7
# 剑指 Offer 45. 把数组排成最小的数
from typing import List

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # a+b>b+a 则a比b“大”
        from functools import cmp_to_key
        return ''.join(sorted(map(str,nums),key=cmp_to_key(lambda x,y: int(x+y) - int(y+x))))

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
