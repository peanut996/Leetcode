#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (50.18%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    96.3K
# Total Submissions: 191.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# from DataStructure import ListNode
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        res = head
        while head is not None and head.next is not None:
            if head.next.val == head.val :
                # 去除与当前元素重复
                head.next = head.next.next
            else:
                # 下移一位
                head = head.next
        return res
# @lc code=end

