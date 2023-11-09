"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        cur = root
        stack = []
        count = 0

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            cur = cur.right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inOrderTraversal(node, res):
            if not node:
                return
            if len(res)-1 == k:
                return
            inOrderTraversal(node.left, res)
            res.append(node.val)
            inOrderTraversal(node.right, res)

        res = []
        inOrderTraversal(root, res)
        return res[k-1]
