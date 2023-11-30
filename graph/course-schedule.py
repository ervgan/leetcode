"""
https://leetcode.com/problems/course-schedule/
"""

# O(n*m)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = {i: [] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        def dfs(crs):
            if crs in visited:
                return False
            if adj_list[crs] == []:
                return True
            visited.add(crs)
            for pre in adj_list[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            adj_list[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
