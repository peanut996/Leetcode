package main

/*235. Lowest Common Ancestor of a Binary Search Tree
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
示例:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6
解释: 节点 2 和节点 8 的最近公共祖先是 6。
*/

/* 算法
1.从根节点开始遍历树
2.如果节点 p 和节点 q 都在右子树上，那么以右孩子为根节点继续 1 的操作
3.如果节点 p 和节点 q 都在左子树上，那么以左孩子为根节点继续 1 的操作
4.如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 p 和节点 q 的 LCA 了
*/
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if q.Val < root.Val && p.Val < root.Val {
		return lowestCommonAncestor(root.Left, p, q)
	}
	if q.Val > root.Val && p.Val > root.Val {
		return lowestCommonAncestor(root.Right, p, q)
	}
	return root
}
