
"""
https://leetcode.com/problems/copy-list-with-random-pointer/
Leetcode 138
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = {}
        ptr = head
        while ptr:
            dic[ptr] = Node(ptr.val, None, None)
            ptr = ptr.next

        ptr = head
        while ptr:
            if ptr.next:
                dic[ptr].next = dic[ptr.next]
            if ptr.random:
                dic[ptr].random = dic[ptr.random]
            ptr = ptr.next

        return dic[head]
