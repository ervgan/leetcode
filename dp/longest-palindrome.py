"""
https://leetcode.com/problems/longest-palindromic-substring/
"""

# O(n2)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        n = len(s)

        def expand(s, left_ptr, right_ptr):
            temp_res = ""
            while left_ptr >= 0 and right_ptr < n and s[left_ptr] == s[right_ptr]:
                temp_res = s[left_ptr:right_ptr+1]
                left_ptr -= 1
                right_ptr += 1
            return temp_res

        for i in range(n):
            odd = expand(s, i, i)
            even = expand(s, i, i+1)
            if len(even) > len(res):
                res = even
            if len(odd) > len(res):
                res = odd

        return res
