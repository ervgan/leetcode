'''
https://leetcode.com/problems/house-robber/
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]

        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 = max(num + prev2, prev1), prev1

        return prev1
