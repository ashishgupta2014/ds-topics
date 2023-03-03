"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

https://www.youtube.com/watch?v=k4eK-vEmnKg
"""
from typing import List


class Solution:

    def dfs(self, prices, i, buy, fee, dp):
        if (i, buy) in dp:
            return dp[(i, buy)]
        if i == len(prices):
            return 0
        if buy == 0:
            profit = max(self.dfs(prices, i+1, 0, fee, dp), -prices[i]+self.dfs(prices, i+1, 1, fee, dp))
        else:
            profit = max(self.dfs(prices, i+1, 1, fee, dp), prices[i]+self.dfs(prices, i+1, 0, fee, dp)-fee)
        dp[(i, buy)] = profit
        return profit
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.dfs(prices, 0, 0, fee, {})

solve = Solution()
print(solve.maxProfit(prices=[1,3,2,8,4,9], fee=2))
