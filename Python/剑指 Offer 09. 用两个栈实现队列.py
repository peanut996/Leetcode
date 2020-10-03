#!/usr/bin/python3.7
# 剑指 Offer 09. 用两个栈实现队列
# from typing import List

class CQueue:

    def __init__(self):
        self.a, self.b = [], []


    def appendTail(self, value: int) -> None:
        self.a.append(value)


    def deleteHead(self) -> int:
        # 辅助栈做法
        if self.b: return self.b.pop()
        if not self.a: return -1
        while self.a:
            self.b.append(self.a.pop())
        return self.b.pop()
    


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
