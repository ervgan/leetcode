"""
https://leetcode.com/problems/invert-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = []
        visited = []
        queue.append(root)
        visited.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp
                if node.left not in visited:
                    visited.append(node.left)
                    queue.append(node.left)
                if node.right not in visited:
                    visited.append(node.right)
                    queue.append(node.right)

        return root

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, root):
        if not root:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.dfs(root.right)
        self.dfs(root.left)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root
