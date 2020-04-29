#!/usr/bin/python3.7

"""33. Search in Rotated Sorted Array
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """解题思路
        二分搜索 首先判断num[0]和num[mid]关系，判断是否有序空间 在判断target是否在有序空间内
        """
        if not nums: 
            return -1
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target: return mid
            # 左边有序
            if nums[0]<=nums[mid]:
                if nums[0]<=target<nums[mid]:
                    r = mid-1
                else:
                    l= mid+1
            # 右边有序
            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    l = mid+1
                else:
                    r= mid -1
                
        return -1

if __name__ == '__main__':

    try:
        assert exec
    except AssertionError:
        print('解答错误')
