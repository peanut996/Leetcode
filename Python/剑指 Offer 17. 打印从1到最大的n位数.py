#!/usr/bin/python3.7

from typing import List
# 剑指 Offer 17. 打印从1到最大的n位数

def printNumbers(self, n: int) -> List[int]:
    return list(i for i in range(1,int('9'*n)+1))

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
