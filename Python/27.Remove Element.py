#!/usr/bin/python3.7
"""
26.移除元素
从数组中删除元素
"""
class Solution(object):
    def removeElement(self, nums, val:int) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums))[::-1]:
            while val in nums:
                nums.remove(val)
        return len(nums)

def main():
    n = [1,2,3,4,4,5,5,5,6,6,7,7,7]
    val = 7
    a = Solution()
    print(Solution.removeElement(a,n,val))

if __name__ == '__main__':
    main()
