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

def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:  # 递归的退出条件
        return
    mid = alist[start]  # 设定起始的基准元素
    low = start  # low为序列左边在开始位置的由左向右移动的游标
    high = end  # high为序列右边末尾位置的由右向左移动的游标
    while low < high:
        # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
    alist[low] = mid  # 将基准元素放到该位置,
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后
