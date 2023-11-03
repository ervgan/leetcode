"""
https://leetcode.com/problems/subtree-of-another-tree/submissions/850160712/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def isSameSubtree(s, t):
            if s and t:
                return s.val == t.val and isSameSubtree(s.left, t.left) and isSameSubtree(s.right, t.right)
            return s is t

        if not root:
            return False
        if isSameSubtree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
