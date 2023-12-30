"""
https://leetcode.com/problems/target-sum/
"""

# O(n*t) where t is the total
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        def backtracking(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in dp:
                return dp[(index, total)]
            dp[(index, total)] = backtracking(index+1, total+nums[index]) + backtracking(index+1, total-nums[index])
            return dp[(index, total)]

        return backtracking(0, 0)
