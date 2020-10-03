#!/usr/bin/python3.7
# 剑指 Offer 66. 构建乘积数组
from typing import List

def constructArr(self, a: List[int]) -> List[int]:
    res , tmp = [1]* len(a),1
    # 两遍连乘
    for i in range(1,len(a)):
        # 左边
        res[i] = res[i-1] * a[i-1]
    for i in range(len(a)-2,-1,-1):
        # 右边
        tmp *= a[i+1]
        res[i] *= tmp
    return res
    # 暴力一行
    # return [reduce(lambda x,y:x*y,a[:i]+a[i+1:]) for i in range(len(a))]

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')


