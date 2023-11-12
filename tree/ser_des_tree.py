"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

# O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("n")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return root
        dfs(root)
        return ','.join(res)




    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.split(',')
        i = [0]
        def dfs():
            if vals[i[0]] == 'n':
                i[0] += 1
                return None
            node = TreeNode(int(vals[i[0]]))
            i[0] += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = []
        queue.append(root)
        res_str = []
        while queue:
            node = queue.pop(0)
            if not node:
                res_str.append('n')
            else:
                res_str.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ','.join(res_str)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = deque([root])
        i = 1

        while i < len(data):
            node = queue.popleft()
            if data[i] != 'n':
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1
            if data[i] != 'n':
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1
        return root
