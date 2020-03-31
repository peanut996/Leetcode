#!/usr/bin/python3.7
"""66. Plus One
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例：
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
"""

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string=''
        for i in digits:
            string+=str(i)
        string=int(string)+1
        digits=[]
        for i in str(string):
            digits.append(int(i))
        return digits

def main():
    digits=[1,2,3]
    solution = Solution()
    try:
        assert solution.plusOne(digits)==[1,2,4]
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
