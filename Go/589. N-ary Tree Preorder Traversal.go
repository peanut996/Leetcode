package main

/*589. N-ary Tree Preorder Traversal
给定一个 N 叉树，返回其节点值的前序遍历。
*/
func preorder(root *Node) []int {
	nums := make([]int, 0)
	var helper func(root *Node, nums *[]int)
	helper = func(root *Node, nums *[]int) {
		if root != nil {
			*nums = append(*nums, root.Val)
			for _, child := range root.Children {
				helper(child, nums)
			}
		}

	}
	helper(root, &nums)
	return nums
}

