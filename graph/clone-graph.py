"""
https://leetcode.com/problems/clone-graph/
"""


# O(n)

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            clone = Node(node.val, [])
            visited[node] = clone
            for neighbor in node.neighbors:
                visited[node].neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited = {}
        node_clone = Node(node.val, [])
        visited[node] = node_clone
        stack = [node]
        while stack:
            cur_node = stack.pop()
            for neighbor in cur_node.neighbors:
                if neighbor not in visited:
                    node_clone = Node(neighbor.val, [])
                    visited[neighbor] = node_clone
                    stack.append(neighbor)
                visited[cur_node].neighbors.append(visited[neighbor])

        return visited[node]
