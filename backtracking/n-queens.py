"""
https://leetcode.com/problems/n-queens/
"""


# O(n!) but in reality better because of pruning
class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        col = set()
        posDiag = set()
        negDiag = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res

class Solution(object):
    def buildFrontier(self, board, n):
        valid_frontier = []
        for i in range(n):
            if self.isOneQueenValid(board, len(board), i):
                valid_frontier.append(board + [i])
        return valid_frontier

    def isOneQueenValid(self, board, target_row, target_col):
        for row, col in enumerate(board):
            if row == target_row or col == target_col or abs(row-target_row) == abs(col-target_col):
                return False
        return True

    def visualize_solution(self, solution):
        visualized = []
        for placement in solution:
            board = []
            for col in placement:
                row_string = "." * col + "Q" + "." * (len(placement) - col - 1)
                board.append(row_string)
            visualized.append(board)
        return visualized

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        cur_board = [0]
        depth = 1
        visited = set()
        def search(cur_board, visited, depth):
            visited.add(tuple(cur_board))
            if depth == n:
                res.append(cur_board)
                return
            possible_next_boards = self.buildFrontier(cur_board, n)
            if possible_next_boards > 0:
                for next_board in possible_next_boards:
                    if tuple(next_board) not in visited:
                        search(next_board, visited, depth+1)

        for i in range(n):
            search([i], visited, depth)

        return self.visualize_solution(res)
