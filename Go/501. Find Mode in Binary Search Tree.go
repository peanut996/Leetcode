package main

/*501. Find Mode in Binary Search Tree
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

    结点左子树中所含结点的值小于等于当前结点的值
    结点右子树中所含结点的值大于等于当前结点的值
    左子树和右子树都是二叉搜索树

例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2

返回[2].

提示：如果众数超过1个，不需考虑输出顺序
*/
func findMode(root *TreeNode) []int {
	nums, maxn, curr, res := []int{}, 1, 1, []int{}
	// 中序遍历
	var inOrder func(root *TreeNode, nums *[]int)
	inOrder = func(root *TreeNode, nums *[]int) {
		if root == nil {
			return
		}
		// 中序遍历
		inOrder(root.Left, nums)
		*nums = append(*nums, root.Val)
		inOrder(root.Right, nums)
	}
	inOrder(root, &nums)

	if len(nums) <= 1 {
		return nums
	}
	res = append(res, nums[0])
	// 取众数
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			curr = 1
		} else {
			curr++
		}
		if curr > maxn {
			res = []int{}
			res = append(res, nums[i])
			maxn = curr
		} else if curr == maxn {
			res = append(res, nums[i])
		}
	}
	return res
}
