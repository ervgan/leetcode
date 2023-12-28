"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""

#O(n), O(n) can make it into O(1) space though
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        sell = [0] * n
        buy = [0] * n
        cool = [0] * n

        buy[0] = -prices[0]

        for i in range(1, n):
            cool[i] = max(cool[i-1], sell[i-1])
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])

        return max(sell[n-1], cool[n-1])
