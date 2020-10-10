#!/usr/bin/python3.7
# 剑指 Offer 44. 数字序列中某一位的数字
# from typing import List

class Solution:
    def findNthDigit(self, n: int) -> int:
        start,count,digit =1,9,1
        # 求是几位数
        while n>count:
            n-=count
            start*=10
            digit += 1
            count = 9*start*digit
        # n-1是因为前面的数位是9会导致起始位为1
        # 求数字是多少
        num = start + (n-1)//digit
        s= str(num)
        # 求数字中的字符是多少
        res = int(s[(n-1)%digit])
        return res

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
