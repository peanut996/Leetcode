#!/usr/bin/python3.7
# 剑指 Offer 59 - I. 滑动窗口的最大值
from typing import List
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # 维持从大到小的队列，保证deque[0]为窗口内最大值的索引
    from collections import deque
    deque,res = deque(),[]
    for index,value in enumerate(nums):
        if deque and deque[0] <= index-k:
            deque.popleft()
        while deque and nums[deque[-1]] < value: 
            deque.pop()
        deque.append(index)
        if index >= k-1:
            res.append(nums[deque[0]])
    return res


if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
