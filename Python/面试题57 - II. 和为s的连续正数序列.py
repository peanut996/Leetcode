#!/usr/bin/python3.7
"""面试题57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例：
输入：9
输出: [[2,3,4],[4,5]]
"""
from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        slow,quick,temp=0,0,0
        queue=[i+1 for i in range(target)]
        result=[]
        for i in range(len(queue)-1):
            slow,quick=i,i+1
            temp=queue[slow]+queue[quick]
            while temp<target:
                quick+=1
                temp+=queue[quick]
            if temp==target:
                result.append(queue[slow:quick+1])
        return result


def main():
    target=9
    solution = Solution()
    try:
        assert solution.findContinuousSequence(target)==[[2,3,4],[4,5]]
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
