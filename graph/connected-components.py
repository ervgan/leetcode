"""

"""

# O(E log V) because amortized and path compression
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parents = [i for i in range(n)]
        rank = [1] * n
        count_connected_comp = 0

        def find(p):
          while p != parents[p]:
            parents[p] = find(parents[p])
            p = parents[p]
          return p

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

        for node1, node2 in edges:
          if union(node1, node2): count_connected_comp += 1

        return n-count_connected_comp


# BFS solution which is O(E + V)
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = set()
        adj_list = {i:[] for i in range(n)}
        res = 0
        queue = []

        for node1, node2, in edges:
          adj_list[node1].append(node2)
          adj_list[node2].append(node1)

        for node in range(n):
          if node not in visited:
            queue.append(node)
            while queue:
              curr_node = queue.pop()
              for child in adj_list[curr_node]:
                if child not in visited:
                  queue.append(child)
                  visited.add(child)
            res += 1

        return res


# Recursive DFS which is also O(E+V)
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = set()
        adj_list = {i:[] for i in range(n)}
        res = 0
        queue = []

        for node1, node2, in edges:
          adj_list[node1].append(node2)
          adj_list[node2].append(node1)

        def dfs(node):
          visited.add(node)
          for child in adj_list[node]:
            if child not in visited:
              visited.add(child)
              dfs(child)


        for node in range(n):
          if node not in visited:
            dfs(node)
            res += 1

        return res
