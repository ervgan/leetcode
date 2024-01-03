"""
https://leetcode.com/problems/distinct-subsequences/
"""

# O(n*m)
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            elif i == len(s):
                return 0
            elif (i, j) in dp:
                return dp[(i,j)]

            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                dp[(i,j)] = dfs(i+1, j)
            return dp[(i, j)]

        return dfs(0, 0)
