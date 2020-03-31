package main

import "math"

// /*104. Maximum Depth of Binary Tree
// 给定一个二叉树，找出其最大深度。
// 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
// 说明: 叶子节点是指没有子节点的节点。

// 示例：
// 给定二叉树 [3,9,20,null,null,15,7]，
//     3
//    / \
//   9  20
//     /  \
//    15   7
// 返回它的最大深度 3 。
// */
// // import "fmt"
// import "math"

// /**
//  * Definition for a binary tree node.
//  * type TreeNode struct {
//  *     Val int
//  *     Left *TreeNode
//  *     Right *TreeNode
//  * }
//  */

var m float64 = 0

//Depth is just a function used in this file.
func Depth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	height := math.Max(float64(Depth(root.Left)), float64(Depth(root.Right)))
	m = math.Max(m, height+1)
	return int(height) + 1
}

func maxDepthofBinary(root *TreeNode) int {
	m = 0
	Depth(root)
	return int(m)
}

// func main() {

// }
