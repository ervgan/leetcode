"""
https://leetcode.com/problems/balanced-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root):
        if not root:
            return True, 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return left[0] and right[0] and abs(left[1] - right[1]) < 2, 1 + max(left[1], right[1])


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)[0]
