"""
https://leetcode.com/problems/permutation-in-string/description/
Leetcode 567. Permutation in String
"""

# Solution 1, O(26 * n), 65 ms
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = 0
        r = len(s1)
        char_dic_s1 = Counter(s1)
        char_dic_s2 = Counter(s2[l:r])
        while r < len(s2):
            if char_dic_s1 == char_dic_s2:
                return True
            char_dic_s2[s2[l]] -= 1
            if char_dic_s2[s2[l]] == 0:
                del char_dic_s2[s2[l]]
            l += 1
            r += 1
            char_dic_s2[s2[r-1]] += 1

        return True if char_dic_s1 == char_dic_s2 else False



# Solution 2, O(n), 37ms
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        matches = 0
        s1_dic, s2_dic = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_dic[ord(s1[i]) - ord('a')] += 1
            s2_dic[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1_dic[i] == s2_dic[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2_dic[index] += 1
            if s1_dic[index] == s2_dic[index]:
                matches += 1
            elif s1_dic[index] + 1 == s2_dic[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2_dic[index] -= 1
            if s1_dic[index] == s2_dic[index]:
                matches += 1
            elif s1_dic[index] - 1 == s2_dic[index]:
                matches -= 1

            l +=1

        return matches==26



