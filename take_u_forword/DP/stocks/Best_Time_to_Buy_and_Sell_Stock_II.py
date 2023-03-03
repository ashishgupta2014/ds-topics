"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

https://www.youtube.com/watch?v=nGJmxkUJQGs

"""
from typing import List

class Solution:

    def dfs(self, prices, i, buy, dp):
        if (i, buy) in dp:
            return dp[(i, buy)]
        if i == len(prices):
            return 0

        if buy == 0:
            profit = max(-prices[i] + self.dfs(prices, i+1, 1, dp), self.dfs(prices, i+1, 0, dp))
        else:
            profit = max(prices[i] + self.dfs(prices, i+1, 0, dp), self.dfs(prices, i+1, 1, dp))
        dp[(i, buy)] = profit
        return profit
    def maxProfit(self, prices: List[int]) -> int:

        return self.dfs(prices, 0, 0, {})
solve = Solution()
print(solve.maxProfit(prices=[7,1,5,3,6,4]))
