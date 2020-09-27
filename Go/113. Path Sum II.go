package main

// 113. Path Sum II
// 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

// 说明: 叶子节点是指没有子节点的节点。

// 示例:
// 给定如下二叉树，以及目标和 sum = 22

func pathSumII(root *TreeNode, sum int) [][]int {
	var res [][]int
	var helper func(root *TreeNode, tmpSum int, temp []int)
	helper = func(root *TreeNode, tmpSum int, temp []int) {
		if root == nil {
			return
		}
		// 不是叶子节点
		if root.Left != nil || root.Right != nil {
			// 剩余值小于当前节点
			temp = append(temp, root.Val)
			helper(root.Left, tmpSum+root.Val, temp)
			helper(root.Right, tmpSum+root.Val, temp)
		} else {
			// 叶子节点
			if sum == (tmpSum + root.Val) {
				temp = append(temp, root.Val)
				tempCopy := make([]int, len(temp))
				copy(tempCopy, temp)
				res = append(res, tempCopy)
			}
		}
	}
	helper(root, 0, []int{})
	return res
}

// func main() {
// 	root := CreateTreefromSlice([]int{-6, -1000, -3, -6, 0, -6, -5, 4, -1000, -1000, -1000, 1, 7})
// 	fmt.Println(pathSumII(root, -21))
// }
