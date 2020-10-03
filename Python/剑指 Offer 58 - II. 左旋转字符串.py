#!/usr/bin/python3.7
# 剑指 Offer 58 - II. 左旋转字符串
# from typing import List

def reverseLeftWords(self, s: str, n: int) -> str:
    # return  s[n:] + s[:n]
    res = ''
    for i in range(n,n+len(s)):
        res += s[i % len(s)]
    return res
    # 不开辟空间做法
    # 先翻转[:n]在翻转[n:]最后翻转全部
if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')


