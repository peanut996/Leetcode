package main

// 111. Minimum Depth of Binary Tree
// 给定一个二叉树，找出其最小深度。
// 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
// 说明: 叶子节点是指没有子节点的节点

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	if root.Left == nil && root.Right == nil {
		return 1
	}

	//这两个结束条件满足'叶结点'要求
	if root.Left == nil && root.Right != nil {
		return minDepth(root.Right) + 1
	}
	if root.Left != nil && root.Right == nil {
		return minDepth(root.Left) + 1
	}
	return Min(minDepth(root.Left), minDepth(root.Right)) + 1

}
