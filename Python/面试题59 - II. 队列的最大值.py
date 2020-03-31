#!/usr/bin/python3.7
"""面试题59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例：
输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]

warning: 此脚本不可运行
"""
class MaxQueue:

    def __init__(self):
        self.l=[]


    def max_value(self) -> int:
        m=0
        if self.l==[]:
            return -1
        else:
            for i in self.l:
                if i>= m:
                    m=i
        return m


    def push_back(self, value: int) -> None:
        self.l.append(value)


    def pop_front(self) -> int:
        if self.l==[]:
            return -1
        else:
            return self.l.pop(0)
            



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

def main():
    solution = Solution()
    try:
        assert exec
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
