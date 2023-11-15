"""
https://leetcode.com/problems/combination-sum/
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        path = []

        def dfs(arr, total, ans, path):
            if total == target:
                ans.append(path)
                return
            if total > target:
                return
            for i in range(len(arr)):
                dfs(arr[i:], total+arr[i], ans, path + [arr[i]])

        dfs(candidates, 0, ans, path)
        return ans


