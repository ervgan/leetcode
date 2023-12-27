"""
https://leetcode.com/problems/longest-common-subsequence/
"""


#O(n*m)
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for row in range(len(text2)-1, -1, -1):
            for col in range(len(text1)-1, -1, -1):
                if text2[row] == text1[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])

        return dp[0][0]
