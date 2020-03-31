package main

/*107. Binary Tree Level Order Traversal II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
*/
// import "fmt"

func levelOrderBottom(root *TreeNode) [][]int {
	var queue []*TreeNode
	var result [][]int
	queue = append(queue, root)
	tag := 0
	if root == nil {
		return result
	}

	//BFS遍历tree得出result[][]
	for len(queue) != 0 {
		length := len(queue)
		for i := 0; i < length; i++ {
			//取出Node
			node := queue[0]

			//存入val
			if len(result) > tag {
				result[tag] = append(result[tag], node.Val)
			} else {
				result = append(result, []int{node.Val})
			}

			//节点入队列
			if node.Left != nil {
				queue = append(queue, node.Left)
			}

			if node.Right != nil {
				queue = append(queue, node.Right)
			}

			//更新队列
			queue = queue[1:]
		}
		//标记更新到下一层
		tag++
	}

	//翻转result数组
	//方法一
	// resultcopy:=make([][]int,0)
	// resultcopy=append(resultcopy,result...)
	// for i,v:=range resultcopy{
	// 	result[len(result)-1-i]=v
	// }

	//方法二
	// for i:=0;i<len(result)/2;i++{
	// 	j:=len(result)-i-1
	// 	result[i],result[j]=result[j],result[i]
	// }

	//方法三
	// left, right := 0, len(result)-1
	// for left < right {
	// 	result[left], result[right] = result[right], result[left]
	// 	left++
	// 	right--
	// }

	return result

}

// func main() {

// }
