"""
https://leetcode.com/problems/minimum-window-substring/
Leetcode 76. Permutation in String
"""

# O(n) time complexity, 500ms
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or t == '' or not s or s == '': return ''

        counter_t = Counter(t)
        counter_s = {}
        have, need = 0, len(counter_t)
        res = float('inf')
        ans = ""
        l = 0
        for r in range(len(s)):
            char = s[r]
            counter_s[char] = 1 + counter_s.get(char, 0)
            if char in counter_t and counter_t[char] == counter_s[char]:
                have += 1

            while have == need:
                if len(s[l:r+1]) < res:
                    ans = s[l:r+1]
                    res = len(s[l:r+1])
                counter_s[s[l]] -= 1
                if s[l] in counter_t and counter_s[s[l]] < counter_t[s[l]]:
                    have -= 1
                l += 1

        return ans if res != float('inf') else ""
