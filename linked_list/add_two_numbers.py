
"""
https://leetcode.com/problems/add-two-numbers/description/
Leetcode 2
"""

#O(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        sum = 0
        res = ListNode(None)
        ans = res
        exp = 0
        if not l1 and not l2:
            return ListNode(None)

        while l1:
            num1 += l1.val * 10**exp
            exp += 1
            l1 = l1.next

        exp = 0
        while l2:
            num2 += l2.val * 10**exp
            exp += 1
            l2 = l2.next

        sum = num1 + num2
        while sum >= 10:
            remainder = sum % 10
            res.next = ListNode(remainder)
            res = res.next
            sum = sum // 10

        res.next = ListNode(sum % 10)
        return ans.next



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(None)
        ptr = ans
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            res = val % 10
            ans.next = ListNode(res)
            ans = ans.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        return ptr.next
