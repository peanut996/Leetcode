package main

/*面试题55 - II. 平衡二叉树 LCOF
注意：本题与主站 110.balanced-binary-tree相同
*/

// func isBalanced(root *TreeNode) bool {
// 	var height func(root *TreeNode) int
// 	height = func(root *TreeNode) int {
// 		if root == nil {
// 			return 0
// 		}
// 		left, right := height(root.Left), height(root.Right)
// 		if left > right {
// 			return left + 1
// 		}
// 		return right + 1
// 	}
// 	if root == nil {
// 		return true
// 	}
// 	// 获取高度差
// 	res := height(root.Left) - height(root.Right)

// 	//判断当前节点以及子节点是否满足
// 	return (res < 2 && res > -2) && isBalanced(root.Left) && isBalanced(root.Right)

// }
