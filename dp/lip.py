"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row, col, prevVal):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or matrix[row][col] <= prevVal:
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            temp_res = 1
            temp_res = max(temp_res, 1 + dfs(row - 1, col, matrix[row][col]))
            temp_res = max(temp_res, 1 + dfs(row + 1, col, matrix[row][col]))
            temp_res = max(temp_res, 1 + dfs(row, col + 1, matrix[row][col]))
            temp_res = max(temp_res, 1 + dfs(row, col - 1, matrix[row][col]))
            dp[row][col] = temp_res
            return temp_res

        lip = 0
        for row in range(ROWS):
            for col in range(COLS):
                lip = max(lip, dfs(row, col, -1))

        return lip
