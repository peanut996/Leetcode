package main

/*590. N-ary Tree Postorder Traversal
给定一个 N 叉树，返回其节点值的后序遍历。
*/

func postorder(root *Node) []int {
	nums := make([]int, 0)
	var helper func(root *Node, nums *[]int)
	helper = func(root *Node, nums *[]int) {
		if root != nil {
			for _, child := range root.Children {
				helper(child, nums)
			}
			*nums = append(*nums, root.Val)
		}

	}
	helper(root, &nums)
	return nums
}
