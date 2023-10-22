
"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1081337662/
Leetcode 19
"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = ListNode(0,head)
        temp = slow
        fast = temp
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return temp.next



class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length == n: return head.next
        ptr = head
        for _ in range(1, length-n):
            ptr = ptr.next
        ptr.next = ptr.next.next

        return head
