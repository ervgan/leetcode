"""
https://leetcode.com/problems/reverse-linked-list/
Leetcode 206
"""


# Iterative method, O(n), 47ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node = head

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next

        return prev


# Recursive method, 21ms
class Solution(object):
    def traverse(self, node, prev):
        if not node:
            return prev
        temp = node.next
        node.next = prev
        return self.traverse(temp, node)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node = head
        return self.traverse(node, prev)
