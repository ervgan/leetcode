"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            max_left = dfs(root.left)
            max_right = dfs(root.right)
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            res[0] = max(res[0], root.val + max_left + max_right)
            return root.val + max(max_left, max_right)

        dfs(root)
        return res[0]



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSumHelper(self, root, ans):
        if not root:
            return 0, ans
        left_sum, ans = self.maxPathSumHelper(root.left, ans)
        right_sum, ans = self.maxPathSumHelper(root.right, ans)
        single_path_sum = max(max(left_sum, right_sum) + root.val, root.val)
        temp_max = max(single_path_sum, left_sum + right_sum + root.val)
        ans = max(temp_max, ans)
        return single_path_sum, ans

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.maxPathSumHelper(root, float('-inf'))[1]
