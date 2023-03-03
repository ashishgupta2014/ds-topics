"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

https://www.youtube.com/watch?v=IGIe46xw3YY
"""
from typing import List


class Solution:

    def dfs(self, prices, i, buy, cap, dp):
        if (i, buy, cap) in dp:
            return dp[(i, buy, cap)]
        if i == len(prices):
            return 0
        if cap != 1:
            if buy == 0:
                profit = max(self.dfs(prices, i+1, 0, 0, dp), -prices[i]+self.dfs(prices, i+1, 1, 0, dp))
            else:
                profit = max(self.dfs(prices, i+1, 1, 0, dp), prices[i]+self.dfs(prices, i+1, 0, 1, dp))
        else:
            profit = self.dfs(prices, i+1, 0, 0 , dp)
        dp[(i, buy, cap)] = profit
        return profit
    def maxProfit(self, prices: List[int]) -> int:
        return self.dfs(prices, 0, 0, 0, {})

solve = Solution()
print(solve.maxProfit(prices=[1,2,3,0,2]))
print(solve.maxProfit(prices=[3,2,6,1, 2,4]))