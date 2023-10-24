"""
https://leetcode.com/problems/linked-list-cycle/description/
"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        ptr1 = head
        ptr2 = head
        while ptr2.next is not None and ptr2.next.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 == ptr2:
                return True

        return False
