
"""
https://leetcode.com/problems/permutations/description/
"""

#O(N×N!) bounded
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        def dfs(curr, ans, path):
            if len(path) == len(nums):
                ans.append(path)
                return
            for i in range(len(curr)):
                dfs(curr[:i] + curr[i+1:], ans, path + [curr[i]])

        dfs(nums, ans, path)
        return ans


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)

        return res
