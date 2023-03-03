"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

https://www.youtube.com/watch?v=-uQGzhYj8BQ
"""
from typing import List


class Solution:

    def dfs(self, prices, i, buy, cap, dp):

        if cap == 0 or i == len(prices):
            return 0

        if (i, buy, cap) in dp:
            return dp[(i, buy, cap)]

        if buy == 0:
            profit = max(self.dfs(prices, i+1, 0, cap, dp) , -prices[i] + self.dfs(prices, i+1, 1, cap, dp))
        else:
            profit = max(self.dfs(prices, i+1, 1, cap, dp), prices[i] + self.dfs(prices, i+1, 0, cap-1, dp))
        dp[(i, buy, cap)] = profit
        return profit

    def tabular(self, prices):
        n = len(prices)
        dp = {}

        for i in range(n-1, -1, -1):
            for buy in range(0, 2):
                for cap in range(1, 3):
                    if buy == 0:
                        profit = max(dp.get((i+1, buy, cap), 0), -prices[i] + dp.get((i+1, buy, cap), 1))
                    else:
                        profit = max(dp.get((i+1, buy, cap), 1), prices[i] + dp.get((i+1, buy, cap-1), 0))
                    dp[(i, buy, cap)] = profit
        return dp
    def maxProfit(self, prices: List[int]) -> int:
        return self.dfs(prices, 0, 0, 2, {})

solve = Solution()
print(solve.maxProfit(prices=[3,3,5,0,0,3,1,4]))
print(solve.maxProfit(prices=[2,1,4,5,2,9,7]))
