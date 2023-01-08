"""
https://workat.tech/problem-solving/practice/best-time-to-buy-and-sell-stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy, sell = 0, 1
        numLength = len(prices)
        maxProfit = 0
        while sell < numLength:
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                if profit > maxProfit:
                    maxProfit = profit
            else:
                buy = sell

            sell += 1
        return maxProfit



solve = Solution()

print(solve.maxProfit(prices=[6, 1, 4, 2, 5, 3]))

print(solve.maxProfit(prices=[5, 4, 3, 2, 1]))