"""
https://leetcode.com/problems/word-break/
"""

#O(n2m)
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        for i in range(n, -1, -1):
            for w in wordDict:
                if i + len(w) <= n and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
