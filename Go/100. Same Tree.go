package main

/*100. Same Tree
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
输出: true
*/
// import "fmt"

//TreeNode Definition for a binary tree node.
// type TreeNode struct {
// 	Val   int
// 	Left  *TreeNode
// 	Right *TreeNode
// }

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	} else if p == nil || q == nil {
		return false
	} else {
		if p.Val != q.Val {
			return false
		}
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

// func main() {
// 	var p, q *TreeNode
// 	p, q = nil, nil
// 	print(isSameTree(q, p))

// }
