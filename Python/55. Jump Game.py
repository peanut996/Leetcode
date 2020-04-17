#!/usr/bin/python3.7
"""55. Jump Game
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i,v in enumerate(nums):
            if i > m : return False
            m = max(m,i+v)
        return True


def main():
    solution = Solution()
    try:
        assert exec
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
