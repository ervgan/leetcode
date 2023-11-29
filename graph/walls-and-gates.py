"""
https://leetcode.com/problems/walls-and-gates/
"""


#O(nm)
from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        visited = set()
        queue = deque()
        nb_rows = len(rooms)
        nb_cols = len(rooms[0])
        dist = 1

        for row in range(nb_rows):
            for col in range(nb_cols):
                if rooms[row][col] == 0:
                    queue.extend([(row+1, col), (row-1, col), (row, col+1), (row, col-1)])
                    visited.add((row, col))

        while queue:
            len_queue = len(queue)
            for _ in range(len_queue):
                row, col = queue.popleft()
                if (row, col) not in visited and row >= 0 and row < nb_rows and col >= 0 and col < nb_cols and rooms[row][col] != -1:
                    rooms[row][col] = dist
                    queue.extend([(row+1, col), (row-1, col), (row, col+1), (row, col-1)])
                visited.add((row, col))
            dist += 1

        return rooms
