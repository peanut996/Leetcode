package main

/*404. Sum of Left Leaves
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
*/

func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	}
	// 左子树为空，则只需遍历右子树
	if root.Left == nil {
		return sumOfLeftLeaves(root.Right)
	}
	// 左结点为叶子节点，则返回左结点+右子树
	if root.Left.Left == nil && root.Left.Right == nil {
		return root.Left.Val + sumOfLeftLeaves(root.Right)
	}
	// 其他情况
	return sumOfLeftLeaves(root.Left) + sumOfLeftLeaves(root.Right)
}
