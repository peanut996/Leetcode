"""[summary]
常用函数与排序
"""
from typing import List


def quick_sort(nums: List[int], start: int, end: int):
    if start >= end:
        return
    left, right = start, end
    pivot = nums[start]
    while left < right:
        while left < right and nums[right] >= pivot:
            right -= 1
        if left < right:
            nums[left] = nums[right]
        while left < right and nums[left] <= pivot:
            left += 1
        if left < right:
            nums[right] = nums[left]
        if left >= right:
            nums[left] = pivot
    quick_sort(nums,start,left -1)
    quick_sort(nums,left+1,end)
