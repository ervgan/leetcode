class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited =  set()
        queue = []
        nb_rows = len(grid)
        nb_cols = len(grid[0])
        count_fresh_orange = 0
        count_fresh_orange_turned_rotten = 0
        minutes = 0

        for row in range(nb_rows):
            for col in range(nb_cols):
                if grid[row][col] == 2:
                    queue.extend([(row-1, col), (row+1, col), (row, col+1), (row, col-1)])
                    visited.add((row, col))
                if grid[row][col] == 1:
                    count_fresh_orange += 1

        if count_fresh_orange == 0:
            return minutes

        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                row, col = queue.pop(0)
                if (row, col) not in visited and row >= 0 and row < nb_rows and col >= 0 and col < nb_cols and grid[row][col] == 1:
                    count_fresh_orange -= 1
                    queue.extend([(row-1, col), (row+1, col), (row, col+1), (row, col-1)])
                    visited.add((row, col))
            minutes += 1

        return minutes-1 if count_fresh_orange == 0 else -1
