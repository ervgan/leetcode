"""
https://leetcode.com/problems/redundant-connection/
"""


# O(E log V) because amortized and path compression
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(p):
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return parents[p]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []

