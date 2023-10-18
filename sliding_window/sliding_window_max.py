"""
https://leetcode.com/problems/sliding-window-maximum/description/
Leetcode 239. Sliding Window Maximum
"""

# O(n)
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deq = deque()
        output = []
        l, r = 0, 0
        n = len(nums)

        while r < n:
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)

            if l > deq[0]:
                deq.popleft()

            if (r+1) >= k:
                output.append(nums[deq[0]])
                l += 1
            r +=1

        return output
