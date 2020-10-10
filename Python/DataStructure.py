# Definition for singly-linked list.
class ListNode:
    """Definition for singly-linked list.
    """
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for binarytree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random