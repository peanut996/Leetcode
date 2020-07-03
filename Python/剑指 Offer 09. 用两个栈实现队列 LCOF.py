#!/usr/bin/python3.7

"""
用两个栈实现一个队列。队列的声明如下，
请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )
"""
# from typing import List

class CQueue:

    def __init__(self):
        self.a, self.b = [], []


    def appendTail(self, value: int) -> None:
        self.a.append(value)


    def deleteHead(self) -> int:
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
