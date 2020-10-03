#!/usr/bin/python3.7
# 剑指 Offer 30. 包含min函数的栈
# from typing import List
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)



    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
        
        


    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()



if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
