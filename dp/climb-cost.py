"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""

# O(n)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]

        first = cost[0]
        second = cost[1]
        for i in range(2, n):
            temp = cost[i] + min(first, second)
            first = second
            second = temp

        return min(first, second)
