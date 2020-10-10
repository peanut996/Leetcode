#!/usr/bin/python3.7
# 剑指 Offer 31. 栈的压入、弹出序列
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack,index = [],0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and popped[index] == stack[-1]:
                stack.pop()
                index += 1
        return not stack
 

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
