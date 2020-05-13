#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# https://leetcode-cn.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (45.27%)
# Likes:    381
# Dislikes: 0
# Total Accepted:    76.3K
# Total Submissions: 168.3K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 删除链表中等于给定值 val 的所有节点。
# 
# 示例:
# 
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
# 
# 
#
from .DataStructure import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ptr = ListNode(0)
        ptr.next = head
        res = ptr
        while ptr.next is not None :
            # 移动next结点
            if ptr.next.val == val :
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return res.next
            
# @lc code=end

