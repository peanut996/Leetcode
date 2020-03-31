package main

/*102. Binary Tree Level Order Traversal
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[[3],[9,20],[15,7]]

*/

func levelOrder(root *TreeNode) [][]int {
	results := [][]int{}
	// tag标记 循环次数 即取出的数量
	tag := 1
	queue := []*TreeNode{}
	queue = append(queue, root)
	for tag != 0 {
		temp := 0
		result := []int{}
		// 取出tag个结点
		for i := 0; i < tag; i++ {
			node := queue[0]
			queue = queue[1:]
			if node != nil {
				result = append(result, node.Val)
				// 此处无需过滤叶节点因为后面拼接数组过滤
				queue = append(queue, node.Left, node.Right)
				temp += 2
			}
		}
		//去除空结果
		if len(result) != 0 {
			results = append(results, result)
		}
		tag = temp

	}
	return results
}
