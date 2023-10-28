# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getKthNode(self, curr, k):
        node = curr
        while node and k > 0:
            node = node.next
            k -= 1
        return node

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        curr = dummy

        while True:
            kthNode = self.getKthNode(curr, k)
            if not kthNode:
                break
            kthNodeNext = kthNode.next

            prev, nxt = kthNode.next, curr.next

            while nxt != kthNodeNext:
                tmp = nxt.next
                nxt.next = prev
                prev = nxt
                nxt = tmp

            tmp = curr.next
            curr.next = kthNode
            curr = tmp

        return dummy.next
