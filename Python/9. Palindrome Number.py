#!/usr/bin/python3.7

# from typing import List
"""9. Palindrome Number
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """回文数不用考虑溢出问题
        """
        if x<0: return False
        cur,num = 0,x
        while num!=0:
            cur = cur *10 + num%10
            num //=10
        return cur==x


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
