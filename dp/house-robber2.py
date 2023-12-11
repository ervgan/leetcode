"""
https://leetcode.com/problems/house-robber-ii/
"""

class Solution(object):
    def helpRob(self, nums):
        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(num + prev2, prev1) , prev1

        return prev1

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.helpRob(nums[:n-1]), self.helpRob(nums[1:n]))
