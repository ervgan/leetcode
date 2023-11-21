"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""



# O(n * 4**n)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        path = ""
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }

        def dfs(path, index):
            if index == len(digits):
                res.append(path)
                return
            char_str = mapping[digits[index]]
            for char in char_str:
                dfs(path + char, index + 1)

        if digits:
            dfs(path, 0)

        return res if digits else []
