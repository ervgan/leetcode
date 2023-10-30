"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = []
        queue.append(root)
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
            depth += 1

        return depth
