#!/usr/bin/python3.7
# 剑指 Offer 59 - II. 队列的最大值
# from typing import List
from collections import deque

class MaxQueue:

    def __init__(self):
        self.deque = deque()
        self.max_deque = deque()

    def max_value(self) -> int:
        return self.max_deque[0] if self.max_deque else -1

    def push_back(self, value: int) -> None:
        self.deque.append(value)
        while self.max_deque and self.max_deque[-1] < value:
            self.max_deque.pop()
        self.max_deque.append(value)
        
    def pop_front(self) -> int:
        if not self.deque: return -1
        res = self.deque.popleft() 
        if res == self.max_deque[0]:
            self.max_deque.popleft()
        return res


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
