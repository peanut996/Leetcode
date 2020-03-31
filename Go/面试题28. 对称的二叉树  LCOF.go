package main

/*面试题28. 对称的二叉树  LCOF
注意：本题与主站 101.symmetric-tree相同
*/
func isSymmetric(root *TreeNode) bool {
	var isMirror func(left *TreeNode, right *TreeNode) bool
	isMirror = func(left *TreeNode, right *TreeNode) bool {
		if left == nil && right == nil {
			return true
		}
		if (left == nil && right != nil) || (left != nil && right == nil) {
			return false
		}

		return left.Val == right.Val && isMirror(left.Left, right.Right) && isMirror(left.Right, right.Left)
	}
	if root != nil {
		return isMirror(root.Left, root.Right)
	}
	return true

}
