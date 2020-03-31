package main

/*面试题27. 二叉树的镜像  LCOF
注意：本题与主站 226.invert-binary-tree相同
*/

func mirrorTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	//翻转
	root.Left, root.Right = root.Right, root.Left
	//递归
	mirrorTree(root.Left)
	mirrorTree(root.Right)
	return root
}
