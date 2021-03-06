package main

/*437. Path Sum III
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
*/
// 双递归
func pathSumIII(root *TreeNode, sum int) int {
	var helper func(root *TreeNode, sum int) int
	// 递归判断某一个节点的所有路径
	helper = func(root *TreeNode, sum int) int {
		if root == nil {
			return 0
		}
		if sum == root.Val {
			return 1 + helper(root.Left, sum-root.Val) + helper(root.Right, sum-root.Val)
		}
		return helper(root.Left, sum-root.Val) + helper(root.Right, sum-root.Val)
	}

	if root == nil {
		return 0
	}
	// 判断所有结点
	return helper(root, sum) + pathSumIII(root.Left, sum) + pathSumIII(root.Right, sum)

}
