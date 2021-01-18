package main

//Max Return Max int
func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

//Min Return min int
func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

/**************************************
 * Functions for tree.
 */

// CreateTreeNode a tree with two nil son.
func CreateTreeNode(val int) *TreeNode {
	return &TreeNode{
		Val:   val,
		Left:  nil,
		Right: nil}
}

//CreateTreefromSlice for creating a Complete Binary Tree from Slice
func CreateTreefromSlice(nums []int) *TreeNode {
	length := len(nums)
	if length == 0 {
		return nil
	}
	head := CreateTreeNode(nums[0])
	queue := []*TreeNode{}
	queue = append(queue, head)
	for i := 1; i < length; {

		//判断队列是否为空
		if len(queue) != 0 {

			//取出头部元素
			node := queue[0]
			queue = queue[1:]

			//判定是否为空结点
			if nums[i] != -1000 {
				node.Left = CreateTreeNode(nums[i])
				queue = append(queue, node.Left)
			}
			i++

			// 手动加一次i<length判定
			if i == length {
				break
			}

			//判断是否为空结点
			if nums[i] != -1000 {
				node.Right = CreateTreeNode(nums[i])
				queue = append(queue, node.Right)
			}
			i++
		} else {
			break
		}
		//取出头元素
	}
	return head
}

// GetSliceFromTree return a Slice
func GetSliceFromTree(root *TreeNode) []int {
	nums := []int{}
	if root == nil {
		return nums
	}
	queue := []*TreeNode{}
	queue = append(queue, root)
	for len(queue) != 0 {
		node := queue[0]
		queue = queue[1:]
		// 取值
		if node != nil {
			//结点入队列
			nums = append(nums, node.Val)
			//去除最外层
			if !(node.Left == nil && node.Right == nil) {
				queue = append(queue, node.Left, node.Right)
			}
		} else {
			nums = append(nums, -1)
		}

	}
	return nums
}

//Height Return the max height of a tree.
func Height(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left, right := Height(root.Left), Height(root.Right)
	if left > right {
		return left + 1
	}
	return right + 1
}

//QuickSort 快速排序
func QuickSort(nums []int, start, end int) {
	if start >= end {
		return
	}
	left, right := start, end
	pivot := nums[left]
	for left < right {
		for left < right && nums[right] >= pivot {
			right--
		}
		if left < right {
			nums[left] = nums[right]
		}
		for left < right && nums[left] <= pivot {
			left++
		}
		if left < right {
			nums[right] = nums[left]
		}
		if left >= right {
			nums[left] = pivot
		}

		QuickSort(nums, start, left-1)
		QuickSort(nums, left+1, end)
	}

}
