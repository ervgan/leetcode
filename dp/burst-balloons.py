"""
https://leetcode.com/problems/burst-balloons/submissions/1137979999/
"""

# O(n3)
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r+1):
                dp[(l, r)] = max(dp[(l, r)], nums[l-1] * nums[i] * nums[r+1] + dfs(l, i-1) + dfs(i+1, r))
            return dp[(l, r)]

        return dfs(1, len(nums)-2)
