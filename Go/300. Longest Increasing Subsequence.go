package main

/*300. Longest Increasing Subsequence
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

说明:
可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 暗示动态规划
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
*/
// import "fmt"

func lengthOfLIS(nums []int) int {
	dp, result := make([]int, len(nums)), 0
	for i := range dp {
		dp[i] = 1
	}
	for i := range nums {
		for j := 0; j < i; j++ {
			if nums[j] < nums[i] {
				//动态规划体现 转移方程nums[i]>nums[j] dp[i]=max(dp[i],dp[j]+1)
				dp[i] = Max(dp[i], dp[j]+1)
			}
		}
		// max函数已定义于Function.go中
		result = Max(dp[i], result)
	}
	return result
}
