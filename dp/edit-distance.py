"""
https://leetcode.com/problems/edit-distance/
"""

# O(n*m)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1)
        n2 = len(word2)
        dp = [[float("inf") for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(n2+1):
            dp[n1][i] = n2 - i
        for j in range(n1+1):
            dp[j][n2] = n1 - j

        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])

        return dp[0][0]
