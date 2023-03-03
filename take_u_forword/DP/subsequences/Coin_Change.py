"""
https://leetcode.com/problems/coin-change/description/

https://www.youtube.com/watch?v=myPeWb3Y68A
"""
from typing import List


class Solution:

    def dfs(self, coins, amount, n, dp):
        if n == 0:
            if amount % coins[n] == 0:
                return amount // coins[n]
            return 10**7
        if dp[n][amount] != -1:
            return dp[n][amount]
        not_take = self.dfs(coins, amount, n - 1, dp)
        take = 10**7
        if coins[n] <= amount:
            take = 1 + self.dfs(coins, amount-coins[n], n, dp)
        dp[n][amount] = min(take, not_take)
        return dp[n][amount]

    def tabulation(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [[-1]*(amount+1) for _ in range(len(coins)+1)]
        # count = self.dfs(coins, amount, len(coins)-1, dp)
        # return -1 if count >= 10**7 else count
        return self.tabulation(coins, amount)

solve = Solution()
print(solve.coinChange(coins=[1,2,5], amount=11))

print(solve.coinChange(coins=[1,2,5], amount=0))

print(solve.coinChange(coins=[2], amount=3))
