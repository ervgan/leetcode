"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""



# O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = []
        if not root:
            return []
        queue.append(root)
        while queue:
            level_nodes = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_nodes)

        return res
