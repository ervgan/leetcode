"""
https://leetcode.com/problems/interleaving-string/description/
"""

# O(n*m)
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        if n1 + n2 != len(s3):
            return False
        dp = [[False for i in range(n1 + 1)]for j in range(n2 + 1)]
        dp[n2][n1] = True

        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                if i < n1 and s1[i] == s3[i+j] and dp[j][i+1]:
                    dp[j][i] = True
                if j < n2 and s2[j] == s3[i+j] and dp[j+1][i]:
                    dp[j][i] = True

        return dp[0][0]
