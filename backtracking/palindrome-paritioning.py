"""
https://leetcode.com/problems/palindrome-partitioning/
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        partition = []
        def isPalindrome(substring):
            left = 0
            right = len(substring) - 1
            while left < right:
                if substring[left] != substring[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(partition, index):
            if index >= len(s):
                res.append(partition)
                return
            for i in range(index, len(s)):
                if isPalindrome(s[index:i+1]):
                    dfs(partition + [s[index:i+1]], i + 1)

        dfs(partition, 0)
        return res
