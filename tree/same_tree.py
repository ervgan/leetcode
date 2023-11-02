"""
https://leetcode.com/problems/same-tree/
"""

# O(min(N,M))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not q or not p:
            return False

        if q.val == p.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = []
        queue.append((p, q))

        while queue:
            node1, node2 = queue.pop(0)
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))

        return True
