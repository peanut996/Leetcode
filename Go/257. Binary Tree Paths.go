package main

import "strconv"

/*257. Binary Tree Paths
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
输入:

   1
 /   \
2     3
 \
  5
输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
*/
func binaryTreePaths(root *TreeNode) []string {
	var (
		results  []string
		TreePath func(*TreeNode, string, *[]string)
	)

	// 闭包定义
	TreePath = func(root *TreeNode, result string, paths *[]string) {
		if root != nil {
			if root.Left == nil && root.Right == nil {
				result += strconv.Itoa(root.Val)
				*paths = append(*paths, result)
			} else {
				result += strconv.Itoa(root.Val) + "->"
				TreePath(root.Left, result, paths)
				TreePath(root.Right, result, paths)
			}
		}
	}

	TreePath(root, "", &results)
	return results
}
