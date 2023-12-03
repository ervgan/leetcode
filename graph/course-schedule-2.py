"""
https://leetcode.com/problems/course-schedule-ii/
"""

#O(V + E)
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list = {i : [] for i in range(numCourses)}
        visited, cycle = set(), set()
        output = []
        for course, prereq  in prerequisites:
            adj_list[course].append(prereq)

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq): return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c): return []

        return output
