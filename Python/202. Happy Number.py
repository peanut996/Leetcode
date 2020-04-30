#!/usr/bin/python3.7

# from typing import List
"""202. Happy Number
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n: int) -> int:
            return sum(list(map(lambda x: int(x)*int(x),str(n))))
        
        slow,quick=n,square(n)
        while slow!=quick:
            slow=square(slow)
            quick=square(square(quick))
        
        return slow==1

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
