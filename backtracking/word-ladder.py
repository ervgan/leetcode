"""
https://leetcode.com/problems/word-ladder/
"""

# adj list takes O(n*m2) and BFS takes O(n2 * m)
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
          return 0

        adj_list = collections.defaultdict(list)
        queue = collections.deque()
        visited = set([beginWord])
        res = 1

        for word in wordList:
          for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            adj_list[pattern].append(word)

        queue.append(beginWord)
        while queue:
          for _ in range(len(queue)):
            word = queue.popleft()
            visited.add(word)
            if word == endWord:
              return res
            for i in range(len(word)):
              pattern = word[:i] + '*' + word[i+1:]
              for neighbor in adj_list[pattern]:
                if neighbor not in visited:
                  queue.append(neighbor)
          res += 1

        return 0
