package main

/*108. Convert Sorted Array to Binary Search Tree
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
*/
// import "fmt"

//升序数组可看做中序遍历二叉搜索树的结果
func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	// 获取中值
	mid := len(nums) / 2
	// 分配子树
	left, right := nums[:mid], nums[mid+1:]
	// 递归
	return &TreeNode{Val: nums[mid], Left: sortedArrayToBST(left), Right: sortedArrayToBST(right)}

}

// func main() {

// }
