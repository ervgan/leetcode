"""
https://leetcode.com/problems/surrounded-regions/description/
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nb_rows = len(board)
        nb_cols = len(board[0])

        def dfs(row, col, visited):
            if (row, col) in visited or row < 0 or row == nb_rows or col < 0 or col == nb_cols or board[row][col] != "O":
                return
            board[row][col] = "T"
            visited.add((row, col))
            dfs(row-1, col, visited)
            dfs(row+1, col, visited)
            dfs(row, col+1, visited)
            dfs(row, col-1, visited)

        for row in range(nb_rows):
            for col in range(nb_cols):
                if board[row][col] == "O" and (row in [0, nb_rows-1] or col in [0, nb_cols-1]):
                    dfs(row, col, set())

        for row in range(nb_rows):
            for col in range(nb_cols):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(nb_rows):
            for col in range(nb_cols):
                if board[row][col] == "T":
                    board[row][col] = "O"

        return board
