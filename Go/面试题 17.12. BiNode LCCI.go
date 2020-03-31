package main

/*面试题 17.12. BiNode LCCI
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求值的顺序保持不变，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
返回转换后的单向链表的头节点。

*/

func convertBiNode(root *TreeNode) *TreeNode {
	var inOrder func(root *TreeNode, prev *TreeNode) *TreeNode
	inOrder = func(root *TreeNode, prev *TreeNode) *TreeNode {
		if root != nil {
			prev = inOrder(root.Left, prev)
			// 更改结点方式
			root.Left = nil
			prev.Right = root
			prev = root
			prev = inOrder(root.Right, prev)
		}
		return prev
	}
	head := &TreeNode{0, nil, nil}
	prev := head
	inOrder(root, prev)
	return head.Right
}
