"""
https://leetcode.com/problems/palindromic-substrings/submissions/1120638600/
"""

# O(n2 )
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        def countPalindromes(left, right):
            temp = 0
            while left >= 0 and right < n and s[left] == s[right]:
                temp += 1
                left -= 1
                right += 1
            return temp

        for i in range(n):
            even = countPalindromes(i, i + 1)
            odd = countPalindromes(i, i)
            res += even + odd
        return res
