from typing import List


class Solution:
    dp = []
    def dfs(self, prices, k, index, buy):
        if k == 0 or index >= len(prices):
            return 0
        if self.dp[k][buy][index] != -1:
            return self.dp[k][buy][index]

        if buy:
                        # buy it == take it                                don't buy == not take it
            profit = max(-prices[index]+self.dfs(prices, k, index+1, 0), 0+self.dfs(prices, k, index+1, 1))
        else:
                        # sell it == take it                             don't sell == not take it
            profit = max(prices[index]+self.dfs(prices, k-1, index+1, 1), 0+self.dfs(prices, k, index+1, 0))
        self.dp[k][buy][index] = profit

        return profit


    def maxProfit(self, prices: List[int], k: int) -> int:
        # self.dp = [[[-1]*(len(prices)+1) for _ in range(2)] for _ in range(k+1)]
        # return self.dfs(prices, k, 0, 1)
        dp = [[[-1] * (len(prices) + 1) for _ in range(2)] for _ in range(k + 1)]

        for i in range(len(prices)-1, -1, -1):
            for buy in range(2):
                for cap in range(1, k+1):
                    if buy:
                        dp[cap][buy][i] = max(-prices[i]+dp[cap][0][i+1], 0+dp[cap][1][i+1])
                    else:
                        dp[cap][buy][i] = max(prices[i]+dp[cap-1][1][i + 1], 0+dp[cap][0][i + 1])

solve = Solution()
print(solve.maxProfit(prices=[6, 1, 4, 2, 5, 3], k=2))
print(solve.maxProfit(prices=[6, 1, 4, 2, 5, 3], k=1))
print(solve.maxProfit(prices=[1, 2, 3, 4, 5], k=4))
print(solve.maxProfit(prices=[1, 2, 3, 4, 5], k=0))

