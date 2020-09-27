package main

// 117. Populating Next Right Pointers in Each Node II
// 给定一个二叉树

// struct Node {
//   int val;
//   Node *left;
//   Node *right;
//   Node *next;
// }
// 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

// 初始状态下，所有 next 指针都被设置为 NULL。

///Definition for a Node.
// type Node struct {
// 	Val   int
// 	Left  *Node
// 	Right *Node
// 	Next  *Node
// }

// func connect(root *Node) *Node {
// 	if root == nil {
// 		return nil
// 	}
// 	queue := []*Node{root}
// 	for len(queue) > 0 {
// 		temp := queue
// 		queue = nil
// 		for index, node := range temp {
// 			if index+1 < len(temp) {
// 				node.Next = temp[index+1]
// 			}
// 			if node.Left != nil {
// 				queue = append(queue, node.Left)
// 			}
// 			if node.Right != nil {
// 				queue = append(queue, node.Right)
// 			}
// 		}
// 	}
// 	return root
// }

// func main() {
// 	fmt.Println("Hello World!")
// }
