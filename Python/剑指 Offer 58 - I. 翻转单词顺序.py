#!/usr/bin/python3.7
# 剑指 Offer 58 - I. 翻转单词顺序
# from typing import List


def reverseWords(self, s: str) -> str:
    s = s.strip()
    i, j, res = len(s)-1,len(s)-1, [] 
    while i>=0:
        while s[i]!=' ': i-=1
        res.append(s[i+1:j+1])
        while s[i] == ' ': i-=1
        j=i
    return ' '.join(res)

# python 一行解法
# def reverseWords(self, s: str) -> str:
#     return ' '.join(s.split()[::-1])

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')


