"""
https://leetcode.com/problems/unique-paths/
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for row in range(n):
            for col in range(m):
                if row-1 >= 0 and col-1 >= 0:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[n-1][m-1]
