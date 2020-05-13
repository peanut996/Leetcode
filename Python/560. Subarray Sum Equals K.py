#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.79%)
# Likes:    391
# Dislikes: 0
# Total Accepted:    40.4K
# Total Submissions: 91.3K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 
# 示例 1 :
# 
# 
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 
# 
# 说明 :
# 
# 
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 
# 
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # slow,fast,length,res = 0,1,len(nums),0
        # while slow < length:
        #     while fast <= length:
        #         if sum(nums[slow:fast]) == k:
        #             res += 1
        #         fast+=1
        #     slow += 1
        #     fast = slow + 1
        # return res

        #  前缀和+哈希表 
        #  sum-k 在hash表中即存在对应的数组 
        Dict = dict({0:1})
        sum,res = 0,0
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in Dict:
                res += Dict[sum-k]
            if sum in Dict:
                Dict[sum] += 1
            else:
                Dict[sum] = 1
        return res


# @lc code=end

