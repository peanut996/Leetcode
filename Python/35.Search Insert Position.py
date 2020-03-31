class Solution:
    def searchInsert(self, nums, target):
        if target not in nums:
            for i in range(len(nums)):
                if nums[i]>target:
                    return i
            return len(nums)
        else:
            return nums.index(target)

def main():
    '''
    test case:
    [1,2,4,5]
    7
    '''
    a=Solution()
    nums=[1,2,4,5]
    target=7
    print(Solution.searchInsert(a,nums,target))

if __name__ == '__main__':
    main()
