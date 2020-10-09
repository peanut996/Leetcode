#!/usr/bin/python3.7
# 剑指 Offer 53 - I. 在排序数组中查找数字 I
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        def binary_search(is_first: bool) -> int:
            left,right =0,length-1
            while left <= right:
                mid = left + (right - left ) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else: 
                    if is_first:
                        if mid > 0 and nums[mid-1] ==nums[mid]:
                            right = mid - 1
                        else:
                            return mid
                    else:
                        if mid < length -1  and nums[mid] == nums[mid+1]:
                            left = mid + 1
                        else:
                            return mid
            return -1
        front,back = binary_search(True),binary_search(False)
        if front == -1:
            return 0
        return 1 if back == front else back - front + 1

if __name__ == '__main__':

    try:
        assert exec
        print('解答正确')
    except AssertionError:
        print('解答错误')
