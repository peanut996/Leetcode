package main

/*110. Balanced Binary Tree
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。
*/
func isBalanced(root *TreeNode) bool {
	var height func(root *TreeNode) int
	height = func(root *TreeNode) int {
		if root == nil {
			return 0
		}
		left, right := height(root.Left), height(root.Right)
		if left > right {
			return left + 1
		}
		return right + 1
	}
	if root == nil {
		return true
	}
	// 获取高度差
	res := height(root.Left) - height(root.Right)

	//判断当前节点以及子节点是否满足
	return (res < 2 && res > -2) && isBalanced(root.Left) && isBalanced(root.Right)

}
