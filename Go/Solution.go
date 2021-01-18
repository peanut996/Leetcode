package main

import "fmt"

//rotate 189.旋转数组
func rotate(nums []int, k int) {
	length := len(nums)
	var newNums = make([]int, length)
	for i := range nums {
		newNums[(i+k)%len(nums)] = nums[i]
	}
}
func verifyPostorder(postorder []int) bool {
	var helper func(i, j int) bool
	helper = func(i, j int) bool {
		if i >= j {
			return true
		}
		pointer := i
		for postorder[pointer] < postorder[j] {
			pointer++
		}
		mid := pointer
		for postorder[pointer] > postorder[j] {
			pointer++
		}

		return pointer == j && helper(i, mid-1) && helper(mid, j-1)
	}
	return helper(0, len(postorder)-1)
}
func main() {
	var nums = []int{1, 3, 5, 7, 9, 2, 4, 6, 8, 0}
	QuickSort(nums, 0, len(nums)-1)
	fmt.Println(nums)
}
