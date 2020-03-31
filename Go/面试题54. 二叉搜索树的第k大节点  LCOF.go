package main

/*面试题54. 二叉搜索树的第k大节点  LCOF
给定一棵二叉搜索树，请找出其中第k大的节点。
*/

func kthLargest(root *TreeNode, k int) int {
	var inOrder func(root *TreeNode, nums *[]int)
	inOrder = func(root *TreeNode, nums *[]int) {
		if root != nil {
			inOrder(root.Left, nums)
			*nums = append(*nums, root.Val)
			inOrder(root.Right, nums)
		}
	}
	nums := make([]int, 0)
	inOrder(root, &nums)
	return nums[len(nums)-k]
}
