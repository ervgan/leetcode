"""
Merge Two Sorted Lists
Leetcode 21
"""

# 0(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(None)
        ans = res
        node1 = list1
        node2 = list2

        while node1 and node2:
            if node1.val < node2.val:
                res.next = ListNode(node1.val)
                node1 = node1.next
            else:
                res.next = ListNode(node2.val)
                node2 = node2.next
            res = res.next

        res.next = node1 or node2

        return ans.next
