"""
https://leetcode.com/problems/max-area-of-island/description/
"""


class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        nb_cols = len(grid[0])
        nb_rows = len(grid)
        max_island_size = 0

        def dfs(r, c):
          if r < 0 or r >= nb_rows or c < 0 or c >= nb_cols or grid[r][c] == 0 or (r, c) in visited:
            return 0
          visited.add((r, c))
          return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1)+ dfs(r, c-1))

        for row in range(nb_rows):
            for col in range(nb_cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    island_size = dfs(row, col)
                    max_island_size = max(max_island_size, island_size)

        return max_island_size

# O(n * m)
class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        nb_cols = len(grid[0])
        nb_rows = len(grid)
        max_island_size = 0

        def bfs(row, col):
            queue = [(row, col)]
            island_size = 0
            while queue:
                r, c = queue.pop(0)
                if r >= 0 and r < nb_rows and c >= 0 and c < nb_cols and grid[r][c] == 1 and (r, c) not in visited:
                    island_size += 1
                    visited.add((r, c))
                    queue.extend([(r+1, c), (r-1, c), (r, c+1), (r, c-1)])
            return island_size

        for row in range(nb_rows):
            for col in range(nb_cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    island_size = bfs(row, col)
                    max_island_size = max(max_island_size, island_size)

        return max_island_size
