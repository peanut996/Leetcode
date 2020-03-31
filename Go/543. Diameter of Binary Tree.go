package main

// /*543. Diameter of Binary Tree
// 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

// 示例 :
// 给定二叉树

//           1
//          / \
//         2   3
//        / \
//       4   5
// 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
// 注意：两结点之间的路径长度是以它们之间边的数目表示。
// */
// import (
// 	"math"
// )

// // TreeNode is a tree definition.
// // type TreeNode struct {
// // 	Val   int
// // 	Left  *TreeNode
// // 	Right *TreeNode
// // }

// // var max int = 0

// func diameterOfBinaryTree(root *TreeNode) int {
// 	//刷新全局变量
// 	max = 0
// 	depth(root)
// 	return max
// }

// func depth(root *TreeNode) int {
// 	if root == nil {
// 		return 0
// 	}
// 	left, right := depth(root.Left), depth(root.Right)
// 	//及时刷新max
// 	max = int(math.Max(float64(max), float64(left+right)))
// 	//递归更新depth
// 	return int(math.Max(float64(left), float64(right))) + 1
// }

// // &TreeNode{Val,Left,Right}
// // func main() {
// // 	root := &TreeNode{Val: 1, Left: &TreeNode{Val: 2, Left: &TreeNode{Val: 4, Left: nil, Right: nil}, Right: &TreeNode{Val: 5, Left: nil, Right: nil}}, Right: &TreeNode{Val: 3, Left: nil, Right: nil}}
// // 	fmt.Println(root)
// // 	fmt.Println(diameterOfBinaryTree(root))
// // }
