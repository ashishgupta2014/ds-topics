"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

https://www.youtube.com/watch?v=IGIe46xw3YY
"""
from typing import List


class Solution:

    def dfs(self, prices, i, buy, cap, dp):
        if (i, buy, cap) in dp:
            return dp[(i, buy, cap)]
        if i == len(prices) or cap == 0:
            return 0
        if buy == 0:
            profit = max(self.dfs(prices, i+1, 0, cap, dp), -prices[i]+self.dfs(prices, i+1, 1, cap, dp))
        else:
            profit = max(self.dfs(prices, i+1, 1, cap, dp), prices[i]+self.dfs(prices, i+1, 0, cap-1, dp))
        dp[(i, buy, cap)] = profit
        return profit
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.dfs(prices, 0, 0, k, {})

solve = Solution()
print(solve.maxProfit(k=2, prices=[2,4,1]))
print(solve.maxProfit(k=2, prices=[3,2,6,5,0,3]))