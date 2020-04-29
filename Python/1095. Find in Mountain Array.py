#!/usr/bin/python3.7

from typing import List
"""1095. Find in Mountain Array
（这是一个 交互式问题 ）

给你一个 山脉数组 mountainArr，请你返回能够使得 mountainArr.get(index) 等于 target 最小 的下标 index 值。

如果不存在这样的下标 index，就请返回 -1。

 

何为山脉数组？如果数组 A 是一个山脉数组的话，那它满足如下条件：

首先，A.length >= 3

其次，在 0 < i < A.length - 1 条件下，存在 i 使得：

A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 
"""

"""
This is MountainArray's API interface.
You should not implement it, or speculate about its implementation
"""
class MountainArray:
   def get(self, index: int) -> int:
       return 0
   def length(self) -> int:
       return 0


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """思路 三个二分查找
        第一个 用于找出山顶
        第二个第三个用于前半部分和后半部分的二分查找
        """

        def binary_search(mountain_arr: 'MountainArray', target: int, l: int, r: int,key=lambda x: x):
            target = key(target)
            while l<=r:
                mid = l + (r-l)//2
                curr = key(mountain_arr.get(mid))
                if curr == target: return mid
                elif curr<target: l=mid+1
                else: r=mid-1
            return -1


        l,r=0,mountain_arr.length()-1
        while l<r:
            mid = l + (r-l)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                # [mid+1,right]
                l= mid+1
            else:
                # [left,mid]
                r=mid
        peak = l
        index = binary_search(mountain_arr,target,0,peak)
        if index != -1:
            return index
        index= binary_search(mountain_arr,target,peak+1,mountain_arr.length()-1,lambda x: -x)
        return index




if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
