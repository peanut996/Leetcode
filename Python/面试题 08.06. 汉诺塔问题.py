#!/usr/bin/python3.7
from typing import List
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """
        def hano(n,A,B,C):
            if n == 1:
                C.append(A.pop())
            else:
                # 从A迁移到B借助C 下面同理
                hano(n-1,A,C,B)
                hano(1,A,B,C)
                hano(n-1,B,A,C)
        hano(len(A),A,B,C)



if __name__ == '__main__':
    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
