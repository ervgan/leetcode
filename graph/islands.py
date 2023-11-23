"""
https://leetcode.com/problems/number-of-islands/
"""


from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nb_rows = len(grid)
        nb_cols = len(grid[0])
        visited = set()
        nb_islands = 0

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            while queue:
                row, col = queue.popleft()
                if row >= 0 and row < nb_rows and col >= 0 and col < nb_cols and grid[row][col] == '1' and (row, col) not in visited:
                    queue.extend([(row+1, col), (row-1, col), (row, col-1), (row, col+1)])
                    grid[row][col] = '0'
                    visited.add((row, col))

        for row in range(nb_rows):
            for col in range(nb_cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    nb_islands += 1
                    bfs(row, col)

        return nb_islands

class Solution(object):
    def explore(self, grid, r, c):
        queue = [(r, c)]
        COLS = len(grid[0])
        ROWS = len(grid)
        visited = set()
        while queue:
            row, col = queue.pop(0)
            if row >= 0 and row < ROWS and col >= 0 and col < COLS and grid[row][col] == "1":
                queue.extend([(row-1, col), (row+1, col), (row, col-1), (row, col+1)])
                grid[row][col] = "0"

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nb_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    nb_islands += 1
                    self.explore(grid, row, col)


        return nb_islands
