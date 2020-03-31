#!/usr/bin/python3.7
"""26.从排序数组中删除重复数据
给定排好序的数组删除重复元素
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums))[::-1]:
            if i-1 != -1:
                if nums[i-1]==nums[i]:
                    del nums[i]
        return len(nums)

def main():
    n = [1,2,3,4,4,5,5,5,6,6,7,7,7]
    a=Solution()
    print(Solution.removeDuplicates(a,n))

if __name__ == '__main__':
    main()