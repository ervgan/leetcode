"""
https://leetcode.com/problems/diameter-of-binary-tree/
"""


# O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    max_diameter = 0
    def diameter(self, root):
        if not root:
            return 0
        left = self.diameter(root.left)
        right = self.diameter(root.right)
        if left + right > self.max_diameter:
            self.max_diameter = left + right
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter(root)
        return self.max_diameter
