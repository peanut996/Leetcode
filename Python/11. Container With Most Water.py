#!/usr/bin/python3.7

"""11. Container With Most Water
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """双指针，每次朝里面移动短板
        数学方法可证明 min(height[i],height[j])*(j-i) 
        朝内移动短板，可能变大
        朝内移动长版板，不变或者变小
        """
        i, j, res = 0, len(height)-1, 0
        while i<j:
            if height[i] < height[j]:
                res = max(res,height[i]*(j-i))
                i+=1
            else:
                res = max(res,height[j]*(j-i))
                j-=1
        return res
        

def main():
    solution = Solution()
    try:
        assert exec
    except AssertionError:
        print('解答错误')


if __name__ == '__main__':
    main()
