package main

/*Definition for all DataStructure like ListNode, TreeNode..

 */

//ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

//TreeNode Definition for a tree.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

//Node Definition for a Node.
type Node struct {
	Val      int
	Children []*Node
}
