"""
https://leetcode.com/problems/coin-change/
"""

#O(nm)
class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for value in range(1, amount+1):
            for coin in coins:
                if value >= coin:
                    dp[value] = min(dp[value-coin]+1, dp[value])

        return dp[-1] if dp[-1] != float('inf') else -1
