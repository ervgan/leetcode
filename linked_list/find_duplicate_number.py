"""
https://leetcode.com/problems/find-the-duplicate-number/
"""

# O(n)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype:
        """
        n = len(nums)
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        return slow
