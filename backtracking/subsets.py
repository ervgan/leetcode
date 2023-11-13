"""
https://leetcode.com/problems/subsets/
"""



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []

        def dfs(i):
            if i >= len(nums):
                res.append(path[:])
                return

            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)

        dfs(0)
        return res
