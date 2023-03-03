"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

https://www.youtube.com/watch?v=excAOvwF_Wk
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return max_profit


solve = Solution()
print(solve.maxProfit(prices=[7,1,5,3,6,4]))
