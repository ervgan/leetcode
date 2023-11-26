"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""


class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        nb_cols = len(heights[0])
        nb_rows = len(heights)
        res = []
        pac, atl = set(), set()
        def dfs(row, col, visit, val):
            if (row, col) in visit or row < 0 or col < 0 or row >= nb_rows  or col >= nb_cols or heights[row][col] < val:
                return
            visit.add((row,col))
            dfs(row-1, col, visit, heights[row][col])
            dfs(row+1, col, visit, heights[row][col])
            dfs(row, col+1, visit, heights[row][col])
            dfs(row, col-1, visit, heights[row][col])

        for c in range(nb_cols):
            dfs(0, c, pac, heights[0][c])
            dfs(nb_rows-1, c, atl, heights[nb_rows-1][c])

        for r in range(nb_rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, nb_cols-1, atl, heights[r][nb_cols-1])

        for r in range(nb_rows):
            for c in range(nb_cols):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])

        return res
