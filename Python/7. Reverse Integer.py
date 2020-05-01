#!/usr/bin/python3.7

# from typing import List

"""7. Reverse Integer
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""

class Solution:
    def reverse(self, x: int) -> int:
        """正确做法 弹入弹出 判断是否溢出
        """
        # y=int(str(x)[::-1]) if x>=0 else -int(str(x)[:0:-1])
        # return y if -2**31<y<2**31-1 else 0

        # 注意负数取余问题
        temp = 0
        isminus=False
        if x<0:
            x=-x
            isminus=True
        while x!=0:
            pop = x%10
            x //=10
            if not -2**31<temp*10 + pop<2**31-1:
                return 0
            temp = temp*10 + pop
        return temp if not isminus else -temp




if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
