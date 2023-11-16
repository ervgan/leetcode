"""
https://leetcode.com/problems/subsets-ii/
"""

#O(n * 2n)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        subset = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1, subset)

        dfs(0, subset)
        return res



class Solution(object):
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

