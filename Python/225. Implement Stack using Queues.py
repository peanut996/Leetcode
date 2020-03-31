"""225. Implement Stack using Queues

使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

warning: 此脚本不可运行
"""
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l=[]


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.l.insert(0,x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.l.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.l[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.l == []:
            return True
        else:
            return False


