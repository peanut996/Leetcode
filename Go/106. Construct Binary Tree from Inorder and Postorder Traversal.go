/*106. Construct Binary Tree from Inorder and Postorder Traversal
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树 [3,9,20,null,null,15,7]*/
package main

func buildTree(inorder []int, postorder []int) *TreeNode {
	indexMap := make(map[int]int)
	for i, v := range inorder {
		indexMap[v] = i
	}

	var helper func(indexLeft, indexRight int) *TreeNode
	helper = func(indexLeft, indexRight int) *TreeNode {
		if indexLeft > indexRight {
			return nil
		}
		val := postorder[len(postorder)-1]
		postorder = postorder[:len(postorder)-1]
		root := &TreeNode{Val: val}

		inorderRootIndex := indexMap[val]
		// 注意这里的后序遍历 所以应该是Right在前
		root.Right = helper(inorderRootIndex+1, indexRight)
		root.Left = helper(indexLeft, inorderRootIndex-1)

		return root
	}
	return helper(0, len(inorder)-1)
}
