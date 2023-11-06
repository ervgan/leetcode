"""
https://leetcode.com/problems/binary-tree-right-side-view/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            res.append(queue[n-1].val)
            for _ in range(n):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return res



#O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildSideView(self, root, res, depth):
        if not root:
            return res
        if depth == len(res):
            res.append(root.val)
        self.buildSideView(root.right, res, depth + 1)
        self.buildSideView(root.left, res, depth + 1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.buildSideView(root, res, 0)
        return res
