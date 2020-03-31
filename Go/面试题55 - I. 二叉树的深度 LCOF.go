package main

import "math"

/*面试题55 - I. 二叉树的深度 LCOF
注意：本题与主站 104.maximum-depth-of-binary-tree

*/

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	res = int(math.Max(float64(maxDepth(root.Left)), float64(maxDepth(root.Right)))) + 1
	return res
}
