package main

/*面试题32 - II. 从上到下打印二叉树 II LCOF
注意：本题与主站 102.binary-tree-level-order-traversal相同
*/

// func levelOrder(root *TreeNode) [][]int {
// 	results := [][]int{}
// 	// tag标记 循环次数 即取出的数量
// 	tag := 1
// 	queue := []*TreeNode{}
// 	queue = append(queue, root)
// 	for tag != 0 {
// 		temp := 0
// 		result := []int{}
// 		// 取出tag个结点
// 		for i := 0; i < tag; i++ {
// 			node := queue[0]
// 			queue = queue[1:]
// 			if node != nil {
// 				result = append(result, node.Val)
// 				// 此处无需过滤叶节点因为后面拼接数组过滤
// 				queue = append(queue, node.Left, node.Right)
// 				temp += 2
// 			}
// 		}
// 		//去除空结果
// 		if len(result) != 0 {
// 			results = append(results, result)
// 		}
// 		tag = temp

// 	}
// 	return results
// }
