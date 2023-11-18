"""
https://leetcode.com/problems/combination-sum-ii/description/
"""


#O(2**n)
class Solution(object):
  def combinationSum2(self, candidates, target):

    ans = []
    candidates.sort()
    path = []

    def backtrack(candidates, ans, path, index, total):
        if total > target:
            return
        if total == target:
            ans.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            backtrack(candidates, ans, path + [candidates[i]], i + 1, total + candidates[i])

        backtrack(candidates, ans, path, 0, 0)
        return ans
