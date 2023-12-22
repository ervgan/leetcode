"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""

# O(n * sum(nums))
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [True] + [False]*s
        for num in nums:
            for curr in range(s, num-1, -1):
                dp[curr] = dp[curr] or dp[curr-num]

        return dp[target]

#set calculates all possible sum partitions
# O(n * sum(nums)), memory complexity is O(sums(nums))
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2:
            return False
        dp = set()
        dp.add(0)
        target = s // 2
        for num in nums:
            temp_dp = set()
            for sub_sum in dp:
                temp_dp.add(sub_sum)
                temp_dp.add(sub_sum + num)
            dp = temp_dp

        return True if target in dp else False

