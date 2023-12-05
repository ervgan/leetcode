"""
https://leetcode.com/problems/graph-valid-tree/
"""


#O(E+V)
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adj_list = {i : [] for i in range(n)}
        visited = set()
        count_nodes = 0

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        def dfs(node, previous):
            if node in visited:
                return False
            visited.add(node)
            for child in adj_list[node]:
                if child == previous:
                    continue
                if not dfs(child, node):
                    return False
            return True

        if dfs(0, -1) and len(visited) == n:
            return True
        return False




