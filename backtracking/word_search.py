"""
https://leetcode.com/problems/word-search/
"""

# O(n*m*4^len(word))
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        res = False
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visited or board[row][col] != word[index]:
                return False

            visited.add((row, col))
            res = dfs(row-1, col, index + 1) or dfs(row+1, col, index+1) or dfs(row, col-1, index+1) or dfs(row, col+1, index+1)
            visited.remove((row, col))
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0): return True

        return False




