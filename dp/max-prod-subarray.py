"""
https://leetcode.com/problems/maximum-product-subarray/
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far, min_so_far = 1, 1
        res = nums[0]
        for num in nums:
            temp_max_so_far = max(num, num*max_so_far, num*min_so_far)
            min_so_far = min(num, num*max_so_far, num*min_so_far)
            max_so_far = temp_max_so_far
            res = max(res, max_so_far)

        return res
