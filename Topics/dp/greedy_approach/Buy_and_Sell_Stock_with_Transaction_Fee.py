"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
"""


class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        memo = {}

        def dfs(index, buy):
            if index >= len(prices):
                return 0

            if (index, buy) in memo:
                return memo[(index, buy)]

            if buy:
                yb = dfs(index + 1, not buy) - prices[index]
                nb = dfs(index + 1, buy)
                res = max(yb, nb)
            else:
                ys = dfs(index + 1, not buy) + prices[index] - fee
                ns = dfs(index + 1, buy)
                res = max(ys, ns)
            memo[(index, buy)] = res
            return res

        return dfs(0, True)


solve = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(solve.maxProfit(prices, fee))

prices = [1, 3, 7, 5, 10, 3]
fee = 3
print(solve.maxProfit(prices, fee))
