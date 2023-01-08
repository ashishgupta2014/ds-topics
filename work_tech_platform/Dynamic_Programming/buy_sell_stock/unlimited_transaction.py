"""
https://workat.tech/problem-solving/practice/best-time-to-buy-and-sell-stock-ii
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        profit = 0
        n = len(prices)
        while buy < n:
            if sell < n and prices[buy] < prices[sell] and profit < (prices[sell] - prices[buy]):
                profit = prices[sell] - prices[buy]
                sell += 1
            else:
                max_profit += profit
                buy = sell
                sell += 1
                profit = 0
        return max_profit

solve = Solution()
print(solve.maxProfit(prices=[6, 1, 4, 2, 5, 3]))

print(solve.maxProfit(prices=[1, 2, 3, 4, 5]))




