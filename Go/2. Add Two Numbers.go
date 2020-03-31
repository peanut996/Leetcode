package main

/*2. Add Two Numbers
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
*/

//大佬做法：递归
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil && l2 == nil {
		return nil
	}
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}

	sum := l1.Val + l2.Val
	nextNode := addTwoNumbers(l1.Next, l2.Next)
	if sum < 10 {
		return &ListNode{Val: sum, Next: nextNode}
	}
	//处理进位 new一个新的节点
	tempNode := &ListNode{
		Val:  1,
		Next: nil,
	}
	return &ListNode{
		Val:  sum - 10,
		Next: addTwoNumbers(nextNode, tempNode),
	}

}

// //我的做法；迭代
// func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
// 	//创建新的链表
// 	head := &ListNode{0, nil}
// 	headcopy := head

// 	//标记位
// 	tag := 0
// 	if l1 == nil && l2 == nil {
// 		return nil
// 	}

// 	//l1,l2同时不空
// 	for l1 != nil && l2 != nil {
// 		v := (l1.Val + l2.Val)

// 		//处理tag
// 		if tag != 0 {
// 			v += tag
// 			tag--
// 		}
// 		//判断是否需要进位
// 		if v >= 10 {
// 			v = v % 10
// 			tag++
// 		}
// 		head.Val = v

// 		//new新的节点
// 		if l1.Next != nil || l2.Next != nil || tag != 0 {
// 			head.Next = &ListNode{0, nil}
// 		}

// 		head, l1, l2 = head.Next, l1.Next, l2.Next
// 	}

// 	//l1不空,l2空
// 	for l1 != nil && l2 == nil {
// 		v := l1.Val
// 		if tag != 0 {
// 			v++
// 			tag--
// 		}
// 		if v >= 10 {
// 			v = v % 10
// 			tag++
// 		}
// 		head.Val = v
// 		if l1.Next != nil || tag != 0 {
// 			head.Next = &ListNode{0, nil}
// 		}
// 		head, l1 = head.Next, l1.Next
// 	}

// 	//l1空，l2不空
// 	for l1 == nil && l2 != nil {
// 		v := l2.Val
// 		if tag != 0 {
// 			v++
// 			tag--
// 		}
// 		if v >= 10 {
// 			v = v % 10
// 			tag++
// 		}
// 		head.Val = v
// 		if l2.Next != nil || tag != 0 {
// 			head.Next = &ListNode{0, nil}
// 		}
// 		head, l2 = head.Next, l2.Next
// 	}

// 	//最后处理tag
// 	if tag != 0 {
// 		head.Val = tag
// 	}
// 	return headcopy
// }
