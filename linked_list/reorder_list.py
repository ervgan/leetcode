"""
https://leetcode.com/problems/reorder-list/
Leetcode 143
"""

# O (n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        curr_list = ListNode(None)
        slow = head
        fast = head
        first = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = self.reverseList(slow.next)
        slow.next = None

        second = mid
        while second:
            temp_first = first.next
            temp_sec = second.next

            first.next = second
            second.next = temp_first

            first = temp_first
            second = temp_sec
